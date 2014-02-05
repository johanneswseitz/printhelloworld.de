#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Johannes Seitz'
SITENAME = u'print("Hello, World!")'
SITEURL = ''

TIMEZONE = 'Europe/Paris'
DATE_FORMATS = {'en': '%Y-%m-%d'}

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ["images", "downloads",]

# Blogroll
LINKS =  (('Stefan Bechtold', 'http://www.bechte.de/'),
          ('Heiko Maaß', 'http://www.heikomaass.de/'),)

THEME = "tuxlite_tbs"

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ookami86'),
          ('Github', 'https://github.com/Ookami86/'),
          ('StackOverflow', 'http://stackoverflow.com/users/641189/johannes'),
          ("Xing", 'https://xing.com/profile/Johannes_Seitz2'),)

TWITTER_USERNAME="Ookami86"

DEFAULT_PAGINATION = 0

DEFAULT_CATEGORY = "Other"

DISQUS_SITENAME = "printhelloworld"

GOOGLE_ANALYTICS = "UA-47774011-1"


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
