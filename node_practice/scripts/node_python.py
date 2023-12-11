#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("python_node")

    rospy.loginfo("Hello, the python node has started")

    rospy.sleep(3)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Info from 10Hz")
        rate.sleep()

