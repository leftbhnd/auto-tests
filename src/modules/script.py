#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import ScriptProcess


class ScriptService:
    def __init__(self):
        '''
        переменные для включения subscribers 
        '''
        self._script_process_subscriber_state = False

        '''
        переменные для геттеров
        '''
        self._script_name = ''
        self._script_state = False

        self._timeout = 0.5

    def scriptProcessListener(self):
        self._script_process_subscriber_state = True
        rospy.Subscriber(
            'script/process', ScriptProcess, self._scriptProcessListener
        )
        rospy.sleep(self._timeout)

    def _scriptProcessListener(self, data):
        if self._script_process_subscriber_state:
            self._script_state = data.process
            self._script_name = data.name
            self._script_process_subscriber_state = False
        rospy.sleep(self._timeout)

    def getScriptProcess(self):
        rospy.sleep(self._timeout)
        return [self._script_name, self._script_state]
