#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import ServoStates


class ServosService:
    def __init__(self):
        '''
        subscribers
        '''
        rospy.Subscriber(
            'promobot_servos/core', ServoStates, self._servoStateListener
        )
        '''
        переменные для геттеров
        '''
        self._servos_state = []

        self._timeout = 0.5

    def _servoStateListener(self, servos):
        self._servos_state = servos.states

    def getServosState(self):
        return self._servos_state
