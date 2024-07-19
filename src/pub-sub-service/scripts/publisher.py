#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def pub_node():
    pub=rospy.Publisher('talker', String, queue_size=5)
    rospy.init_node('pub_node', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        str_to_be_pub = "EECE 5554"
        rospy.loginfo("PA1 publisher node is running")
        pub.publish(str_to_be_pub)
        rate.sleep()
        

if __name__ == '__main__':
    try:
        pub_node()
    except rospy.ROSInterruptException:
        pass








