#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Erik'
SITENAME = u'qa7.ru'
SITEURL = 'http://qa7.ru'

SITE_AUTHOR = 'Erik Khalimov'
TWITTER_USERNAME = '@biomehanik'
GOOGLE_PLUS_URL = 'https://plus.google.com/+ErikKhalimov'
INDEX_DESCRIPTION = 'Website and blog of Erik Khalimov, a developer and tester from Moscow, RU.'
BIO_TEXT = 'Blog about programming, testing and life'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'

#DISQUS_SITENAME = 'biomaks-github-io'

GOOGLE_FONTS = [
    "Raleway:400,600",
    "Source Code Pro",
]

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'develop'
PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = u'ru'
THEME = "./themes/pneumatic"
MD_EXTENSIONS = ['codehilite(linenums = True)', 'extra']

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

STATIC_PATHS = ['images', 'uploads', 'extra', 'extra/CNAME']
IGNORE_FILES = ['.DS_Store']
extras = ['CNAME', 'favicon.ico', 'keybase.txt', 'robots.txt']
EXTRA_PATH_METADATA = {'extra/%s' % file: {'path': file} for file in extras}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['assets', 'neighbors', 'gallery', 'better_figures_and_images', 'liquid_tags.img', 'sitemap']
RESPONSIVE_IMAGES = True
FIGURE_NUMBERS = True

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

SIDEBAR_LINKS = [
    '<a href="/about/">About</a>',
    '<a href="/projects/">Projects</a>',
]

ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
    ('cache', False),
    ('manifest', False),
    ('url_expire', False),
    ('versions', False),
]

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
SOCIAL_ICONS = [
    ('mailto:biomaks@gmail.com', 'Email', 'fa-envelope'),
    ('http://twitter.com/biomehanik', 'Twitter', 'fa-twitter'),
    ('http://plus.google.com/+ErikKhalimov', 'Google+', 'fa-google-plus-square'),
    ('http://github.com/biomaks', 'GitHub', 'fa-github'),
    ('atom.xml', 'RSS', 'fa-rss')
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://pages.github.com">GitHub&nbsp;Pages</a>.'
