"""
test_url.py is the test library correpsonding to the url.py file.
"""
__author__ = 'Ian Stephenson'

import os
import re
import sys
import unittest
import http.client

sys.path.append(os.pardir)
import src.url


class URLTestSuite(unittest.TestCase):
    response = None
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

    def setUp(self):
        URLTestSuite.response = src.url.posturl(src.url.websoc_url, self.websoc_form_data)

    def test_geturl_sends_valid_request(self):
        response_data = URLTestSuite.response.read().decode('utf-8')
        self.assertIsNotNone(URLTestSuite.response)
        self.assertIsInstance(URLTestSuite.response, http.client.HTTPResponse)
        self.assertEqual(URLTestSuite.response.getcode(), 200)
        self.assertIsNotNone(re.match('<!DOCTYPE\s+html', response_data))  # Make sure it returns HTML

    def test_posturl_retrieves_class_listings(self):
        response_data = URLTestSuite.response.read().decode('utf-8')
        print(response_data)
        self.assertIsNotNone(re.search('<div\s+class="course-list">', response_data))


if __name__ == '__main__':
    unittest.main()