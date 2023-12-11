#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node("publisher_py")
    pub = rospy.Publisher("message_topic", String, queue_size=1000)
    rate = rospy.Rate(10)

    rospy.loginfo("Node started")
    
    while not rospy.is_shutdown():
        msg = String()
        msg.data = "This is a message to publish"
        pub.publish(msg)
        rate.sleep()