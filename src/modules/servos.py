#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import ServoStates


class ServosService:
    def __init__(self):
        '''
        переменные для включения subscribers 
        '''
        self._servos_state_subscriber_state = False
        '''
        переменные для геттеров
        '''
        self._servos_state = []

        self._timeout = 0.5

    def servoStateListener(self):
        self._servos_state = []
        self._servos_state_subscriber_state = True
        rospy.Subscriber(
            'promobot_servos/core', ServoStates, self._servoStateListener
        )
        rospy.sleep(self._timeout)

    def _servoStateListener(self, data):
        if self._servos_state_subscriber_state:
            self._servos_state.append(data.states)
            self._servos_state_subscriber_state = False
        rospy.sleep(self._timeout)

    def getServosState(self):
        rospy.sleep(self._timeout)
        return self._servos_state