#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16, Float32
import csv
import os

filename = os.path.join(os.path.dirname(__file__), '../../data.csv')

def create_file():
    f = open(filename, 'w')
    writer = csv.writer(f)
    writer.writerow(['Raw', '/q'])
    f.close()

def append_row(row):
    f = open(filename, 'a')
    writer = csv.writer(f)
    writer.writerow(row)
    f.close()

def publish_kthfs_result(result):
    pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
    pub.publish(result)

def callback(data):
    q = 0.15
    result = data.data / q

    publish_kthfs_result(result)

    append_row([data.data, result])

def listener():

    rospy.init_node('nodeB', anonymous=True)

    create_file()

    rospy.Subscriber('reimer', Int16, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
