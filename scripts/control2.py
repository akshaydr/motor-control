#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

fr = 0.00
fl = 0.00
br = 0.00
bl = 0.00

speed = 3.142   # radians/sec i.e 30degrees per second

if __name__ == '__main__':
  pub = rospy.Publisher('joint_states', JointState, queue_size=10)
  rospy.init_node('control2')
  # rate = rospy.Rate(10)  # 10hz

  joint_state = JointState()
  joint_state.header = Header()
  joint_state.name = ['base_to_wheel1', 'base_to_wheel2',
                      'base_to_wheel3', 'base_to_wheel4']

  rate = 40.0  # in Hz
  step = speed / rate

  # print(step)

  while not rospy.is_shutdown():
    joint_state.header.stamp = rospy.Time.now()
    joint_state.position = [fr, fl, br, bl]
    # joint_state.velocity = [1, 1, 1, 1]

    if(1):  # forward
      fr += step
      fl += step
      br += step
      bl += step
    else if(2):  # backward
      fr -= step
      fl -= step
      br -= step
      bl -= step
    else if(3):  # left
      fr -= step
      fl += step
      br -= step
      bl += step
    else if(4):  # right
      fr += step
      fl -= step
      br += step
      bl -= step

  # print(joint_state)

  pub.publish(joint_state)

  rospy.sleep(1 / rate)
