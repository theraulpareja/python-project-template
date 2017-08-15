#! /usr/bin/env python

#Common modules for testing
#import sys
#sys.path.append('../src')
#import unittest
#import logging
#import os
#import pdb

log_name = 'some.log'

class TesXXXXX(unittest.TestCase):

    def setUp(self): 
        """Example, creates the logger object"""

    def tearDown(self):
        """Exmaple deletes the log file"""
        try:
            os.remove(log_name)
        except Exception:
            pass

    #Some other tests below
    def test_XXXXX(self):
        """Tests log file is being created"""


if __name__ == '__main__':
    unittest.main(exit=False)
