#!/usr/bin/env python3
import rospy
from rospy_tutorials.srv import AddTwoInts

def callback(req):
    rospy.loginfo("Sum "+str(req.a + req.b))
    return req.a + req.b

if __name__ == '__main__':
    rospy.init_node('add_int_server')

    server = rospy.Service("/add_two_ints", AddTwoInts, callback)
    rospy.loginfo("dfhgcg")
    rospy.spin()