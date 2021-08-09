#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from sensor_msgs.msg import Joy
from std_msgs.msg import Empty


class JoyService:
    def __init__(self):
        '''
        publishers
        '''
        self._pub_joy_phrase_mode = rospy.Publisher(
            'joy/speech/switch', Empty, latch=True, queue_size=10
        )

        self._pub_joy_cmd = rospy.Publisher(
            'joy', Joy, latch=True, queue_size=10)

        self._timeout = 0.5

    def joyPhraseModePub(self):
        self._pub_joy_phrase_mode.publish()
        rospy.sleep(self._timeout)

    def joyCommandPub(self, commands):
        for command in commands:
            joy = Joy()
            joy.header.frame_id = ''
            joy.header.stamp = rospy.get_rostime()
            joy.axes = command['axes']
            joy.buttons = command['buttons']
            self._pub_joy_cmd.publish(joy)
            rospy.sleep(self._timeout)
