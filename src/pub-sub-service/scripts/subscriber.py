#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def sub_callback(data):
    rospy.loginfo(" %s is an awesome class", data.data)

def sub_node():
    rospy.init_node('sub_node', anonymous=True)
    rospy.Subscriber('talker', String, sub_callback)
    rospy.spin()

if __name__ == '__main__':
    sub_node()
