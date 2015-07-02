#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rami Taibah'
SITENAME = u"Rami's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Riyadh'

DEFAULT_LANG = u'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/rtaibah'),
          ('Keybase', 'http://keybase.io/rami'),
	  ('Github', 'http://github.com/rtaibah'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Summary Max Length
SUMMARY_MAX_LENGTH = 50

# Ignore cache
LOAD_CONTENT_CACHE = False

# Display sub-pages in the menu
DISPLAY_PAGES_ON_MENU = True
