#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import ScriptProcess


class ScriptService:
    def __init__(self):
        '''
        subscribers
        '''
        rospy.Subscriber(
            'script/process', ScriptProcess, self._scriptProcessListener
        )
        '''
        переменные для геттеров
        '''
        self._script_name = ''
        self._script_state = False

        self._scr_timeout = 0.5

    def _scriptProcessListener(self, script):
        rospy.sleep(self._scr_timeout)
        self._script_state = script.process
        self._script_name = script.name

    def getScriptProcess(self):
        return [self._script_name, self._script_state]
