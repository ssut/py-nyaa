import re
from collections import namedtuple

URL_NYAA = 'http://www.nyaa.se/'
NyaaResult = namedtuple('NyaaResult',
    ['title', 'category', 'link', 'guid', 'date',
     'seeders', 'leechers', 'downloads', 'size', ])
FORMAT_DATETIME = '%a, %d %b %Y %H:%M:%S %z'
RE_DESC = re.compile(
    r'(?P<seeders>[\d]+) seeder\(s\), (?P<leechers>[\d]+) leecher\(s\), (?P<downloads>[\d]+) download\(s\) - (?P<size>[\d\.]+) (?P<format>[\w]+)',
    re.IGNORECASE)

class SortBy:
    DATE = 1
    SEEDERS = 2
    LEECHERS = 3
    DOWNLOADS = 4
    SIZE = 5
    NAME = 6

    @classmethod
    def vars(cls):
        local = [var for var in dir(cls) if not callable(var) and not '_' in var]
        return local
