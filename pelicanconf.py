#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'ThiaguinhoLS'
SITENAME = 'Diário de um programador'
SITEURL = ''
THEME = 'temas/minimalist'
PATH = 'content'
DISQUS_SITENAME = 'diariodeumprogramador'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

LOAD_CONTENT_CACHE = False

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SOCIAL = (
    ('stack-overflow', 'https://pt.stackoverflow.com/users/88315/thiagoluizs'),
    ('github', 'https://github.com/ThiaguinhoLS/'),
    ('twitter', 'https://twitter.com/ThiaguinhoLS3'),
    ('facebook', 'thiagoluizs@yahoo.com'),
)

GITHUB_URL = 'http://github.com/ThiaguinhoLS'
TWITTER_URL = 'https://twitter.com/ThiaguinhoLS3'
FACEBOOK_URL = 'https://facebook.com/thiagoluizs'

PYGMENTS_RST_OPTIONS = {
    'classprefix': 'pgcss',
    'linenos': 'table'
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

