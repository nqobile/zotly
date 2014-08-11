"""
test_url.py is the test library correpsonding to the url.py file.
"""
__author__ = 'Ian Stephenson'

import unittest
import urllib.request
import urllib.parse


class URLTestSuite(unittest.TestCase):
    websoc_url = 'http://websoc.reg.uci.edu/perl/WebSoc'
    websoc_form_data = {'Submit':           'Display Web Results',
                        'YearTer':          '2014-92',
                        'ShowComments':     'on',
                        'ShowFinals':       'on',
                        'Breadth':          'ANY',
                        'Dept':             'I&C SCI',
                        'CourseNum':        '',
                        'Division':         'ANY',
                        'CourseCodes':      '',
                        'InstrName':        '',
                        'CourseTitle':      '',
                        'ClassType':        'ALL',
                        '&Units':           '',
                        'Days':             '',
                        'StartTime':        '',
                        'EndTime':          '',
                        'MaxCap':           '',
                        'FullCourses':      'ANY',
                        'FontSize':         '100',
                        'CancelledCourses': 'Exclude',
                        'Bldg':             '',
                        'Room':             ''}
    request = None
    respose = None

    def setUp(self):
        urlencoded_websoc_form_data = urllib.parse.urlencode(self.websoc_form_data)
        binary_websoc_form_data = urlencoded_websoc_form_data.encode('utf-8')
        self.request = urllib.request.Request(self.websoc_url, data=binary_websoc_form_data, method='POST')
        self.response = urllib.request.urlopen(self.request)

    def test_geturl_sends_valid_request(self):
        self.assertIsNotNone(self.request)
        self.assertIsNotNone(self.response)
        r = self.response.read().decode('utf-8')
        print(r)

if __name__ == '__main__':
    unittest.main()