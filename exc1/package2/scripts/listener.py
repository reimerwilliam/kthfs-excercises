#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16, Float32

def publishKthfsResult(result):
    pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
    rospy.loginfo("Publishing result: " + str(result))
    pub.publish(result)

def callback(data):
    q = 0.15
    result = data.data / q
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', result)

    publishKthfsResult(result)

def listener():

    rospy.init_node('nodeB', anonymous=True)

    rospy.Subscriber('reimer', Int16, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
