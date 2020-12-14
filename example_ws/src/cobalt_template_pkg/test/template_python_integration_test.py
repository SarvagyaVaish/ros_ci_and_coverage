#!/usr/bin/env python

import unittest
import rospy
from std_msgs.msg import String

from cobalt_utils.ros_topic import MostRecentSubscriber


class TemplatePythonIntegrationTest(unittest.TestCase):
    def test_chatter(self):
        chatter_sub = MostRecentSubscriber("chatter", String)
        chatter_msg = None

        while chatter_msg is None:
            chatter_msg = chatter_sub.get_recent()
            rospy.sleep(0.25)

        self.assertTrue(True)


if __name__ == "__main__":
    import rostest

    rospy.init_node("template_python_integration_test")
    rostest.rosrun("cobalt_template_pkg", "template_python_integration_test", TemplatePythonIntegrationTest)
