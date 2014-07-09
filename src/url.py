"""
url.py is a wrapper for all http events and related methods
"""
__author__ = 'Ian Stephenson'

import urllib.request


def download_url(url_to_open):
    # urllib.request.openurl() returns a bytes object w/ iso-8859-1 charset encoding
    return urllib.request.urlopen(url_to_open).read()
