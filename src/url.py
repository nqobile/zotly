"""
url.py is a wrapper for all http events and methods that are related
"""
__author__ = 'Ian Stephenson'


import urllib.request


def download_url(url_to_open):
	return urllib.request.urlopen(url_to_open).read()  # urllib.request.openurl() returns a bytes object w/ iso-8859-1 charset encoding