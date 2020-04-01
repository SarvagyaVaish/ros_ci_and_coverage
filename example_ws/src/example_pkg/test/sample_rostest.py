#!/usr/bin/env python

import unittest

import rospy
import rostest


class SampelRostest(unittest.TestCase):
    def test_smoke(self):
        self.assertTrue(True)

    def test_smoke_2(self):
        self.assertTrue(False)


if __name__ == "__main__":
    rospy.init_node("sim_test_cases")
    rostest.rosrun("example_pkg", "sample_rostest", SampelRostest)
