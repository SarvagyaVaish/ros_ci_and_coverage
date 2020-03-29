#!/usr/bin/env python

import unittest

from example_pkg.utils import get_time_str


class TestUtils(unittest.TestCase):
    def test_get_time_str(self):
        """
        Smoke test for get_time_str
        """
        get_time_str()
        self.assertTrue(True)
