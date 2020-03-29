#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo("Received: {}".format(data.data))


def listener():
    rospy.init_node("subscriber_node", anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()


if __name__ == "__main__":
    listener()
