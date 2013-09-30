#!/usr/bin/env python3

import unittest
from TiaCloudStorage import TiaCloudStorage

class TestTiaCloudStorage(unittest.TestCase):

    def test_createAnInstance(self):
        TiaCloudStorage()

if __name__ == '__main__':
    unittest.main()
