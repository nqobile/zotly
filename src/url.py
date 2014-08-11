__author__ = 'Ian Stephenson'

import unittest
import urllib.request
import urllib.parse


websoc_url = 'http://websoc.reg.uci.edu/perl/WebSoc'


def posturl(url, post_data):
    # Returns a url response returned to the post request according to the url and post_data parameters
    urlencoded_post_data = urllib.parse.urlencode(post_data)
    binary_post_data = urlencoded_post_data.encode('utf-8')
    request = urllib.request.Request(url, data=binary_post_data)
    return urllib.request.urlopen(request)
