# Py-Nyaa!

[![Build Status](https://travis-ci.org/ssut/py-nyaa.svg?branch=master)](https://travis-ci.org/ssut/py-nyaa)
[![PyPI version](https://badge.fury.io/py/nyaa.svg)](http://badge.fury.io/py/nyaa)

A Nyaa.se client library.

Compatible with both Python 2.7 and 3.4.

## Installation

Stable release:

```bash
$ pip install nyaa
```

Development release:

```bash
$ git clone git://github.com/ssut/nyaa.git
$ cd nyaa && python setup.py install
```

## Usage

First:

```python
In [1]: from nyaa import nyaa
```

Basic usage:

```python
In [2]: nyaa.search('horrible subs')[:5]
Out[2]:
[NyaaResult(title=u'[HorribleSubs] Takamiya Nasuno Desu! - 11 [720p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=701758', guid=u'http://www.nyaa.se/?page=view&tid=701758', date=datetime.datetime(2015, 6, 15, 17, 32, 20), seeders=239, leechers=12, downloads=3186, size=28626125),
 NyaaResult(title=u'[HorribleSubs] Takamiya Nasuno Desu! - 11 [480p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=701757', guid=u'http://www.nyaa.se/?page=view&tid=701757', date=datetime.datetime(2015, 6, 15, 17, 32, 20), seeders=59, leechers=2, downloads=1004, size=13002342),
 NyaaResult(title=u'[HorribleSubs] Teekyu S4 - 47 [720p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=701756', guid=u'http://www.nyaa.se/?page=view&tid=701756', date=datetime.datetime(2015, 6, 15, 17, 30, 21), seeders=179, leechers=12, downloads=2527, size=28311552),
 NyaaResult(title=u'[HorribleSubs] Teekyu S4 - 47 [480p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=701755', guid=u'http://www.nyaa.se/?page=view&tid=701755', date=datetime.datetime(2015, 6, 15, 17, 30, 15), seeders=30, leechers=3, downloads=705, size=12897485),
 NyaaResult(title=u'[HorribleSubs] Kaitou Joker - 24 [1080p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=701746', guid=u'http://www.nyaa.se/?page=view&tid=701746', date=datetime.datetime(2015, 6, 15, 17, 0, 53), seeders=61, leechers=9, downloads=725, size=592026010)]
```

With some sweeeet options:

```python
In [3]: nyaa.search('horrible subs', offset=1, order='-seeders')[:5]
Out[3]:
[NyaaResult(title=u'[HorribleSubs] Fate Stay Night - Unlimited Blade Works - 23 [720p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=701028', guid=u'http://www.nyaa.se/?page=view&tid=701028', date=datetime.datetime(2015, 6, 13, 17, 30, 40), seeders=1348, leechers=61, downloads=35144, size=337956045),
 NyaaResult(title=u'[HorribleSubs] DanMachi - 11 [720p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=700615', guid=u'http://www.nyaa.se/?page=view&tid=700615', date=datetime.datetime(2015, 6, 12, 17, 30, 40), seeders=1339, leechers=40, downloads=38886, size=337746330),
 NyaaResult(title=u'[HorribleSubs] Shokugeki no Soma - 11 [720p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=700665', guid=u'http://www.nyaa.se/?page=view&tid=700665', date=datetime.datetime(2015, 6, 12, 19, 27, 16), seeders=1150, leechers=47, downloads=33323, size=356096410),
 NyaaResult(title=u'[HorribleSubs] Naruto Shippuuden - 416 [720p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=700263', guid=u'http://www.nyaa.se/?page=view&tid=700263', date=datetime.datetime(2015, 6, 11, 11, 0, 40), seeders=1093, leechers=46, downloads=29917, size=330930586),
 NyaaResult(title=u'[HorribleSubs] Seraph of the End - 11 [720p].mkv', category=u'English-translated Anime', link=u'http://www.nyaa.se/?page=download&tid=700949', guid=u'http://www.nyaa.se/?page=view&tid=700949', date=datetime.datetime(2015, 6, 13, 14, 0, 30), seeders=1061, leechers=48, downloads=31345, size=463470592)]
```

The following strings are available for the parameter `order`:

`date`, `seeders`, `leechers`, `downloads`, `size`, `name`

**NOTE**: If you add subtraction operator as the first char of the parameter, the results will be ordered in a descending sequence.

## License

MIT License. See LICENSE file for details.


