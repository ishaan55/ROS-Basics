#!/usr/bin/env python3
import rospy
from rospy_tutorials.srv import AddTwoInts

if __name__ == '__main__':
    rospy.init_node("add_two_ints_client")
    rospy.wait_for_service("/add_two_ints")

    try:
        add_two_ints_service = rospy.ServiceProxy("/add_two_ints", AddTwoInts)
        res = add_two_ints_service(12, 5)
        rospy.loginfo("Sum "+str(res.sum))
    except:
        rospy.loginfo("Failed")