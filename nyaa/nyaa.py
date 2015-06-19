# -*- coding: utf-8 -*-
import requests
import xmltodict
from datetime import datetime, timedelta

from .constants import URL_NYAA, FORMAT_DATETIME, RE_DESC, PY3
from .constants import SortBy, Filters
from .constants import NyaaResult
_agent = requests.Session()

def search(keyword='', offset=1, **kwargs):
    order = kwargs.get('order', '-date')
    filter = kwargs.get('filter', 'none')
    user = kwargs.get('user', '')
    if isinstance(user, int):
        user = str(user)

    sort = order.replace('-', '')
    sorts = SortBy.vars()
    for var in sorts:
        if var == sort.upper():
            sort = getattr(SortBy, var)
            break
    if not isinstance(sort, int):
        return ValueError('The value "order" you passed is not of the correct value.')

    filters = Filters.vars()
    for var in filters:
        if var == filter.upper():
            filter = getattr(Filters, var)
            break
    if not isinstance(filter, int):
        return ValueError('The value "filter" you passed is not of the correct value.')

    order = '2' if order[:1] != '-' else ''
    params = {
        'page': 'rss',
        'term': keyword,
        'offset': offset,
        'sort': sort,
        'order': order,
        'filter': filter,
        'user': user,
    }

    resp = _agent.get(URL_NYAA, params=params)
    xml = xmltodict.parse(resp.text)
    try:
        items = xml['rss']['channel']['item']
    except KeyError:
        return []

    if 'title' in items:
        items = [items]

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
    return (int(matches['seeders']),
            int(matches['leechers']),
            int(matches['downloads']),
            int(size))

def _parse_datetime(text):
    dt = None
    if PY3:
        dt = datetime.strptime(text, FORMAT_DATETIME)
    else:
        text, tz = text.rsplit(' ', 1)
        dt = datetime.strptime(text, FORMAT_DATETIME)
        tz = int(tz)
        tz = timedelta(hours=tz / 100, minutes=tz % 100)
        dt += tz

    return dt
