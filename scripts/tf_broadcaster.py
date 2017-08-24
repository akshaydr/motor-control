#!/usr/bin/env python

import tf
import rospy


if __name__ == '__main__':
  rospy.init_node('tf_broadcaster')

  rate = rospy.Rate(10.0)

  i = 0.0
  
  while not rospy.is_shutdown():
    i +=0.01
    bf = tf.TransformBroadcaster()
    bf.sendTransform((0,i,0),
                     tf.transformations.quaternion_from_euler(0,0,0),
		     rospy.Time.now(),
                     'wheel_2',
		     'base_link')
    rate.sleep()
