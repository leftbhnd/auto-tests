#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import ScriptProcess
from std_msgs.msg import Empty


class ScriptService:
    def __init__(self):
        '''
        publishers
        '''
        self._pub_script_cancel = rospy.Publisher(
            'script/cancel', Empty, latch=True, queue_size=10
        )
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
        self._script_process = False

        self._timeout = 0.5

    def cancelScriptPub(self):
        empty_msg = Empty()
        self._pub_script_cancel.publish(empty_msg)
        rospy.sleep(self._timeout)

    def _scriptProcessListener(self, script):
        self._script_process = script.process
        self._script_name = script.name

    def getScriptProcess(self):
        return [self._script_process, self._script_name, ]
