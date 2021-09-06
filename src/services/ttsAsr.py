#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import ASRResult
from promobot_msgs.msg import Answer
from promobot_msgs.msg import TTSCommand
from std_msgs.msg import Empty


class TtsAsrService:
    def __init__(self):
        '''
        publishers
        '''
        self._pub_text_to_asr = rospy.Publisher(
            'asr/result', ASRResult, latch=True, queue_size=10
        )
        self._pub_text_to_tts = rospy.Publisher(
            'tts/start', TTSCommand, latch=True, queue_size=10
        )
        self._pub_cancel_speech = rospy.Publisher(
            'tts/cancel', Empty, latch=True, queue_size=10
        )
        '''
        subscribers
        '''
        rospy.Subscriber(
            'answers/answer', Answer, self._answersListener
        )
        rospy.Subscriber(
            'tts/start', TTSCommand, self._ttsListener
        )
        '''
        переменные для геттеров
        '''
        self._robot_answer = ''
        self._robot_speech = ''

        self._asr_timeout = 0.8

    def asrPub(self, data):
        asr_result = ASRResult()
        asr_result.header.frame_id = "asr"
        asr_result.header.stamp = rospy.get_rostime()
        asr_result.source = 0
        asr_result.uuid = data.uuid
        asr_result.text = data.text
        asr_result.final = 1
        asr_result.conf = 1.0
        self._pub_text_to_asr.publish(asr_result)
        rospy.sleep(self._asr_timeout)

    def _answersListener(self, answer):
        rospy.sleep(self._asr_timeout)
        self._robot_answer = answer.replica.text

    def getAnswer(self):
        rospy.sleep(self._asr_timeout)
        return self._robot_answer

    def cancelSpeechPub(self):
        empty_msg = Empty()
        self._pub_cancel_speech.publish(empty_msg)
        rospy.sleep(self._asr_timeout)

    def ttsPub(self, data):
        tts_command = TTSCommand()
        tts_command.text = data.text
        tts_command.terminate = False
        tts_command.uuid = data.uuid
        tts_command.ignore_saving = False
        self._pub_text_to_tts.publish(tts_command)
        rospy.sleep(self._asr_timeout)

    def _ttsListener(self, speech):
        rospy.sleep(self._asr_timeout)
        self._robot_speech = speech.text

    def getTts(self):
        return self._robot_speech

    def getLevelsOrder(self):
        rospy.sleep(self._asr_timeout)
        levels_order = rospy.get_param('answers/levels_order')
        return levels_order

    def getSystemLanguage(self):
        rospy.sleep(self._asr_timeout)
        system_language = rospy.get_param('system/language')
        return system_language
