#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo("data : " + str(msg.data))


rospy.init_node('topic_subscriber')

pub = rospy.Subscriber('counter', Int32, callback)

rospy.spin()