#!/usr/bin/env python
"""Basic Python interface to the IMDB iPhone JSON api.
setup.py copied/edited from dbr's tvdb_api
"""
from setuptools import setup
setup(
name = 'imdb',
version='0.1',

author=['dbr/Ben', 'MinRK'],
description='JSON Interface to imdb.com',
url='http://github.com/minrk/IMDb-Python-API',
license='BSD',

long_description="""\
A simple JSON interface to imdb.com
Basic usage is:

>>> import imdb_api
>>> show = imdb_api.Series('My Name Is Earl')
>>> ep = show[1][22]
>>> ep
{u'release_date': {u'normal': u'2006-04-27'},
 u'tconst': u'tt0782419',
 u'title': u'Stole a Badge',
 u'type': u'tv_episode',
 u'year': u'2006'}
>>> movie = imdb_api.Movie('The Dark Knight')
 
""",

py_modules = ['imdb_api'],

classifiers=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Berkeley Software Distribution (BSD)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Multimedia",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
)
