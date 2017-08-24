#!/usr/bin/env python

import tf
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

dirr = 0
angle = Twist()


def callback(data_res):
  global angle
  angle = data_res


if __name__ == '__main__':

  rospy.init_node('tf_broad3')
  sub = rospy.Subscriber('rotation2', Twist, callback)
  rate = rospy.Rate(20.0)

  bf = tf.TransformBroadcaster()
  bf.sendTransform((0, 0, 0),
                   tf.transformations.quaternion_from_euler(0, 0, 0),
                   rospy.Time.now(),
                   'shaft_link',
                   'rotation_link')

  count = 0
  while not rospy.is_shutdown():
    # print(angle.angular.z)
    bf.sendTransform((0, 0, 0),
                     tf.transformations.quaternion_from_euler(
        angle.angular.x, angle.angular.y, 		     angle.angular.z),
        rospy.Time.now(),
        'shaft_link',
        'base_link')
    rate.sleep()
