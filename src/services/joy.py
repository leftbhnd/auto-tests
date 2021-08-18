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
            'joy', Joy, latch=True, queue_size=10
        )
        '''
        subscribers
        '''
        rospy.Subscriber(
            'joy', Joy, self._joyListener
        )
        '''
        переменные для геттеров
        '''
        self._joy_axes = []
        self._joy_buttons = []

        self._timeout = 0.5

    def joyPhraseModePub(self):
        empty_msg = Empty()
        self._pub_joy_phrase_mode.publish(empty_msg)
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

    def _joyListener(self, joy_cmd):
        self._joy_axes = joy_cmd.axes
        self._joy_buttons = joy_cmd.buttons

    def getJoyCmd(self):
        return [self._joy_axes, self._joy_buttons]
