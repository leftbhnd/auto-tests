#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import ASRResult
from promobot_msgs.msg import Answer
from promobot_msgs.msg import TTSCommand
from promobot_srvs.srv import SetLinguoLevels
from std_msgs.msg import Empty
from src.helpers.messages import AsrTtsMsg


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

        self._timeout = 0.8

    def asrPub(self, text):
        asr_result = ASRResult()
        asr_msg = AsrTtsMsg(text)
        asr_result.header.frame_id = "asr"
        asr_result.header.stamp = rospy.get_rostime()
        asr_result.source = 0
        asr_result.uuid = asr_msg.uuid
        asr_result.text = asr_msg.text
        asr_result.final = 1
        asr_result.conf = 1.0
        self._pub_text_to_asr.publish(asr_result)
        rospy.sleep(self._timeout)

    def _answersListener(self, answer):
        self._robot_answer = answer.replica.text

    def getAnswer(self):
        rospy.sleep(self._timeout)
        return self._robot_answer

    def cancelSpeechPub(self):
        empty_msg = Empty()
        self._pub_cancel_speech.publish(empty_msg)
        rospy.sleep(self._timeout)

    def ttsPub(self, text):
        tts_command = TTSCommand()
        tts_msg = AsrTtsMsg(text)
        tts_command.text = tts_msg.text
        tts_command.terminate = False
        tts_command.uuid = tts_msg.uuid
        tts_command.ignore_saving = False
        self._pub_text_to_tts.publish(tts_command)
        rospy.sleep(self._timeout)

    def _ttsListener(self, speech):
        self._robot_speech = speech.text

    def getTts(self):
        return self._robot_speech

    def getLevelsOrder(self):
        rospy.sleep(self._timeout)
        levels_order = rospy.get_param('answers/levels_order')
        return levels_order

    def getSystemLanguage(self):
        rospy.sleep(self._timeout)
        system_language = rospy.get_param('system/language')
        return system_language

    def changeLevel(self, levels):
        rospy.wait_for_service('answers/levels/set')
        set_params = rospy.ServiceProxy('answers/levels/set', SetLinguoLevels)
        resp = set_params([levels, False])
        return 'heeeellooooooo'
