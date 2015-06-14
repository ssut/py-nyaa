# -*- coding: utf-8 -*-
import requests
import xmltodict
from datetime import datetime

from .constants import URL_NYAA, FORMAT_DATETIME, RE_DESC
from .constants import SortBy
from .constants import NyaaResult
_agent = requests.Session()

def search(keyword='', offset=1, order='-date'):
    sort = order.replace('-', '')
    sorts = SortBy.vars()
    for var in sorts:
        if var == sort.upper():
            sort = getattr(SortBy, var)
            break
    if not isinstance(sort, int):
        return ValueError('The value "order" you passed is not of the correct value.')

    order = '2' if order[:1] != '-' else ''
    params = {
        'page': 'rss',
        'term': keyword,
        'offset': offset,
        'sort': sort,
        'order': order,
    }

    resp = _agent.get(URL_NYAA, params=params)
    xml = xmltodict.parse(resp.text)
    items = xml['rss']['channel']['item']

    results = []
    for item in items:
        seeders, leechers, downloads, size = _parse_desc(item['description'])
        data = {
            'title': item['title'],
            'category': item['category'],
            'link': item['link'],
            'guid': item['guid'],
            'date': _parse_datetime(item['pubDate']),
            'seeders': seeders,
            'leechers': leechers,
            'downloads': downloads,
            'size': size,
        }
        result = NyaaResult(**data)
        results.append(result)

    return results

def _parse_size(size, fmt='bytes'):
    units = {
        'TIB': 1024 ** 4,
        'GIB': 1024 ** 3,
        'MIB': 1024 ** 2,
        'KIB': 1024,
        'B': 1,
        'BYTE': 1,
        'BYTES': 1,
    }
    return round(size * units[fmt.upper()])

def _parse_desc(text):
    matches = [m.groupdict() for m in RE_DESC.finditer(text)][0]
    size = _parse_size(float(matches['size']), matches['format'])
    return (matches['seeders'], matches['leechers'], matches['downloads'], size)

def _parse_datetime(text):
    dt = datetime.strptime(text, FORMAT_DATETIME)
    return dt