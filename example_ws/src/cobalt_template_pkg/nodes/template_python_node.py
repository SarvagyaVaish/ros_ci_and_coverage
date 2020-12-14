#!/usr/bin/env python

import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    rospy.init_node('template_python_node')
    pub = rospy.Publisher('chatter', String, queue_size=10)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
