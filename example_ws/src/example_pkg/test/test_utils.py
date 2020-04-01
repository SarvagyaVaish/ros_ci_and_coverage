#!/usr/bin/env python

import unittest

from example_pkg.utils import get_time_str, foo_bar_2


class TestUtils(unittest.TestCase):
    def test_get_time_str(self):
        """
        Smoke test for get_time_str
        """
        get_time_str()
        self.assertTrue(True)

    def test_foo_bar_2(self):
        """
        Smoke test for foo_bar_2
        """
        foo_bar_2()
        self.assertTrue(True)
