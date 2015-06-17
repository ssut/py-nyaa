import re
import sys
from collections import namedtuple

PY3 = sys.version_info >= (3, 3)

URL_NYAA = 'http://www.nyaa.se/'
NyaaResult = namedtuple('NyaaResult',
    ['title', 'category', 'link', 'guid', 'date',
     'seeders', 'leechers', 'downloads', 'size', ])
FORMAT_DATETIME = '%a, %d %b %Y %H:%M:%S{}'.format(' %z' if PY3 else '')
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
        local = [var for var in dir(cls) if not callable(var) and not var.startswith('_')]
        return local

class Filters:
    NONE = 0
    REMAKRS = 1
    TRUSTED = 2
    A_PLUS = 3

    @classmethod
    def vars(cls):
        local = [var for var in dir(cls) if not callable(var) and not var.startswith('_')]
        return local
