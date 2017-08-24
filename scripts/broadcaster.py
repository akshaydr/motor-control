#!/usr/bin/env python

import tf
import rospy

count = 0
if __name__ == '__main__':
    rospy.init_node('broadcaster')



  while not rospy.is_shutdown():
    rospy.init_node('tf_broad2')
    rate = rospy.Rate(10.0)
    bf = tf.TransformBroadcaster()
    bf.sendTransform((0, 0, 0),
                     tf.transformations.quaternion_from_euler(count, 0, 0),
                     rospy.Time.now(),
                     'shaft_link',
                     'base_link')
    sub = rospy.Subscriber('rotation', String, callback)
