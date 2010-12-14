#!/usr/bin/env python
# encoding: utf-8
"""
search.py

Provides functions to interact with the search feature of the IMDb iPhone API.
"""

from __future__ import absolute_import

import urllib

from .base import Imdb

def search(term, extra=None):
    i = Imdb()

    arg = {"q": term}
    if extra:
        arg.update(extra)
    return i.make_request('/find', arg)
