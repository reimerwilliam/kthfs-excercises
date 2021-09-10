#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

def talker():
    pub = rospy.Publisher('reimer', Int16, queue_size=10)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(20) # 20hz
    k = 1
    n = 4
    while not rospy.is_shutdown():
        rospy.loginfo("k: " + str(k))
        pub.publish(k)
        k += n
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
