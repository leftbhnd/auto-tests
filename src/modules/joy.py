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

        self._joy_cmd_subscriber_state = False

        self._joy_cmd = []

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

    def joyListener(self):
        rospy.sleep(self._timeout)
        self._joy_cmd = []
        self._joy_cmd_subscriber_state = True
        rospy.Subscriber(
            'joy', Joy, self._joyListener
        )

    def _joyListener(self, data):
        if self._joy_cmd_subscriber_state:
            self._joy_cmd.append(data.axes)
            self._joy_cmd.append(data.buttons)
            self._joy_cmd_subscriber_state = False

    def getJoyCmd(self):
        rospy.sleep(self._timeout)
        return self._joy_cmd
