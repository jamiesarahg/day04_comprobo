#!/usr/bin/env python
"""This is a proportional control test"""
#https://floobits.com/rifkinni/Day_03_Nicole_Josh/file/emergency_stop.py:12

import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

class Proportional_controller(object):
  def __init__(self):

    rospy.init_node('proportional_control')


    self.error = 0
    self.gain = 1
    self.target_distance = 2
    
    self.twist = Twist()
    self.scan = LaserScan()

    rospy.Subscriber("/scan", LaserScan, self.wallErrorCalc)
    self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)



  def wallErrorCalc(self, data):
    self.error = data.ranges[0] - self.target_distance
    self.twist.linear.x = self.error*self.gain
    self.pub.publish(self.twist)
    print self.twist

  def run(self):
    r = rospy.Rate(5)
    while not rospy.is_shutdown():
        r.sleep()


if __name__ == '__main__':
  run = Proportional_controller()
  run.run()

      