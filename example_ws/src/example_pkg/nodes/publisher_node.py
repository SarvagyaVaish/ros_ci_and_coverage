#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import example_pkg.measure_coverage
from example_pkg.utils import get_time_str


def loop():
    pub = rospy.Publisher("chatter", String, queue_size=10)
    rospy.init_node("publisher_node")
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg_str = "Hello world. Today is {}.".format(get_time_str())
        rospy.loginfo("Publishing: {}".format(msg_str))
        pub.publish(msg_str)
        rate.sleep()


if __name__ == "__main__":
    try:
        loop()
    except rospy.ROSInterruptException as e:
        rospy.logerr("Exception: {}".format(repr(e)))
