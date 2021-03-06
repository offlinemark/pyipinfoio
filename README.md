# pyipinfoio

Simple python wrapper around the [ipinfo.io](http://ipinfo.io) API.

## Usage

```
>>> import pyipinfoio
>>> ip = pyipinfoio.IPLookup()
>>> ip.lookup('8.8.8.8')
{u'loc': u'38.0000,-97.0000', u'city': None, u'country': u'US', u'region': None, u'hostname': u'google-public-dns-a.google.com', u'ip': u'8.8.8.8', u'org': u'AS15169 Google Inc.'}
>>> ip.lookup('8.8.8.8')['country']
u'US'
>>> ip.lookup('8.8.8.8', 'country')
'US'
```

## Installation

If you have [pip](https://pypi.python.org/pypi/pip) simply run:

```bash
$ pip install pyipinfoio
```

If you don't, get pip. Or do it the hard way:

```bash
$ python setup.py install
```

## Dependencies

You need to have [curl](http://curl.haxx.se/) installed. To check if you do, run `which curl` and if nothing comes back, you don't have it and need to install it. For OS X, use [homebrew](http://brew.sh) and on Ubuntu, use `sudo apt-get install curl`.
