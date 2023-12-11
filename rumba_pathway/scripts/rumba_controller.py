#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
from turtlesim.msg import Pose
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty

current_pos = Pose2D()
cmd = Twist()


rospy.init_node("rumba_pose")
pub_cmd_vel = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1000)
client_pose = rospy.ServiceProxy("/turtle1/teleport_absolute", TeleportAbsolute)
client_empty = rospy.ServiceProxy("/clear", Empty)

def callback(pos):

    current_pos.x = pos.x
    current_pos.y = pos.y
    rospy.loginfo(f"{current_pos.x:.3f},{current_pos.y:.3f}")

    
    if current_pos.x > 10:
        cmd.linear.x = 0.8
        cmd.angular.z = 1.2
    elif current_pos.x < 1:
        cmd.linear.x = 0.8
        cmd.angular.z = -1.2
    elif current_pos.y > 10:
        client_pose(1,1,0)
        client_empty()
    else:
        cmd.linear.x = 3.5
        cmd.angular.z = 0
    pub_cmd_vel.publish(cmd)


sub_pose = rospy.Subscriber("/turtle1/pose", Pose, callback)
rospy.spin()