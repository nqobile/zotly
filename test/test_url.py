"""
test_url.py is the test library correpsonding to the url.py file.
"""
__author__ = 'Ian Stephenson'

import unittest
import urllib.error

from src import url


class URLTestSuite(unittest.TestCase):

	def test_download_url_raises_exception_for_invalid_url(self):
		self.assertRaises(urllib.error.URLError, url.download_url, 'hppt://g.o.o.g.l.e..c.o.m.')

	def test_download_url_returns_an_html_document(self):
		websoc_html = url.download_url('http://websoc.reg.uci.edu/perl/WebSoc')
		self.assertEqual(websoc_html[10:14].decode('iso-8859-1'), 'html')  # Tests the DOCTYPE header to be html

	def test_download_url_returns_a_bytes_object(self):
		websoc_html = url.download_url('http://websoc.reg.uci.edu/perl/WebSoc')
		self.assertIsInstance(websoc_html, bytes)

	def test_download_url_bytes_object_is_encoded_in_iso_8859_1(self):
		websoc_html = url.download_url('http://websoc.reg.uci.edu/perl/WebSoc')
		websoc_html.decode('iso-8859-1')  # This test should throw a UnicodeDecodeError if the encoding is not iso-8859-1
		self.assertEquals


if __name__ == '__main__':
	unittest.main()