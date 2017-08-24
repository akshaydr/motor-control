#!/usr/bin/env python

import tf
import rospy
from geometry_msgs.msg import Twist

count = 0
angle = Twist()


def callback(data_res):
  global count
  global angle
  angle = data_res
  if angle.angular.z == 2:
    count += 1
    print count
    bf = tf.TransformBroadcaster()
    bf.sendTransform((0, 0, 0),
                     tf.transformations.quaternion_from_euler(count, 0, 0),
                     rospy.Time.now(), 'wheel_1', 'base_link')
  if angle.angular.z == -2:
    count -= 1
    print count
    bf = tf.TransformBroadcaster()
    bf.sendTransform((0, 0, 0),
                     tf.transformations.quaternion_from_euler(count, 0, 0),
                     rospy.Time.now(), 'wheel_1', 'base_link')
  if angle.linear.x == 2:
    count += 1
    print count
    bf = tf.TransformBroadcaster()
    bf.sendTransform((0, 0, 0),
                     tf.transformations.quaternion_from_euler(count, 0, 0),
                     rospy.Time.now(), 'wheel_1', 'base_link')
  if angle.linear.x == -2:
    count -= 1
    print count
    bf = tf.TransformBroadcaster()
    bf.sendTransform((0, 0, 0),
                     tf.transformations.quaternion_from_euler(count, 0, 0),
                     rospy.Time.now(), 'wheel_1', 'base_link')
  print angle.linear


if __name__ == '__main__':
  angle = Twist()
  rospy.init_node('control')
  bf = tf.TransformBroadcaster()
#  bf = tf.TransformBroadcaster()
  sub = rospy.Subscriber('turtle1/cmd_vel', Twist, callback)
  rospy.spin()
