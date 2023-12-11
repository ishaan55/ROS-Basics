#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def Callback(msg):
    rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node("Subscriber_py")
    rospy.loginfo("Subscriber started!")

    sub = rospy.Subscriber('message_topic', String, Callback)
    rospy.spin()