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

 Trusted Only or A+ Only:
 
```python
In [4]: nyaa.search('fate stay night', filter='a_plus')[:5]
Out[4]:
[NyaaResult(title='[UTW]_Fate_stay_night_Unlimited_Blade_Works_-_22_[h264-720p][0FF31339].mkv', category='English-translated Anime', link='http://www.nyaa.se/?page=download&tid=699412', guid='http://www.nyaa.se/?page=view&tid=699412', date=datetime.datetime(2015, 6, 8, 13, 24, 11, tzinfo=datetime.timezone.utc), seeders=168, leechers=2, downloads=11318, size=288987546),
 NyaaResult(title='[UTW]_Fate_stay_night_Unlimited_Blade_Works_-_21_[h264-720p][25371AA1].mkv', category='English-translated Anime', link='http://www.nyaa.se/?page=download&tid=698248', guid='http://www.nyaa.se/?page=view&tid=698248', date=datetime.datetime(2015, 6, 5, 12, 49, 24, tzinfo=datetime.timezone.utc), seeders=137, leechers=4, downloads=9715, size=467140608),
 NyaaResult(title='[UTW]_Fate_stay_night_Unlimited_Blade_Works_-_20_[h264-720p][A1CCC196].mkv', category='English-translated Anime', link='http://www.nyaa.se/?page=download&tid=696241', guid='http://www.nyaa.se/?page=view&tid=696241', date=datetime.datetime(2015, 5, 30, 13, 11, 8, tzinfo=datetime.timezone.utc), seeders=114, leechers=2, downloads=10618, size=441660211),
 NyaaResult(title='[UTW]_Fate_stay_night_Unlimited_Blade_Works_-_19_[h264-720p][79AE9907].mkv', category='English-translated Anime', link='http://www.nyaa.se/?page=download&tid=692283', guid='http://www.nyaa.se/?page=view&tid=692283', date=datetime.datetime(2015, 5, 18, 22, 59, 23, tzinfo=datetime.timezone.utc), seeders=110, leechers=2, downloads=12427, size=305555046),
 NyaaResult(title='[UTW]_Fate_stay_night_Unlimited_Blade_Works_-_18_[h264-720p][A53F5445].mkv', category='English-translated Anime', link='http://www.nyaa.se/?page=download&tid=690424', guid='http://www.nyaa.se/?page=view&tid=690424', date=datetime.datetime(2015, 5, 14, 12, 31, 45, tzinfo=datetime.timezone.utc), seeders=86, leechers=4, downloads=11748, size=515794534)]
```
 
The following strings are available for the parameter `filter`:

`remarks`, `trusted`, `a_plus`
 

The following strings are available for the parameter `order`:

`date`, `seeders`, `leechers`, `downloads`, `size`, `name`

**NOTE**: If you add subtraction operator as the first char of the parameter, the results will be ordered in a descending sequence.

## License

MIT License. See LICENSE file for details.


