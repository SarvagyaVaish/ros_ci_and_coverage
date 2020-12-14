#!/usr/bin/env python

import unittest


class TemplatePythonUnitTest(unittest.TestCase):

    def test_smoke(self):
        self.assertTrue(True)


if __name__ == "__main__":
    import rostest

    rostest.rosrun("cobalt_template_pkg", "template_python_unit_test", TemplatePythonUnitTest)
