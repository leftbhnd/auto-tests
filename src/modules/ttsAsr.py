#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import ASRResult
from promobot_msgs.msg import Answer
from promobot_msgs.msg import TTSCommand
from std_msgs.msg import Empty


class TtsAsr:
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
        переменные для включения subscribers 
        '''
        self._answer_subscriber_state = False
        '''
        переменные для геттеров 
        '''
        self._robot_answer = ''
        self._levels_order = rospy.get_param('answers/levels_order')

        self._timeout = 0.5

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
        rospy.sleep(self._timeout)

    def answersListener(self):
        rospy.sleep(self._timeout)
        self._robot_answer = ''
        self._answer_subscriber_state = True
        rospy.Subscriber(
            'answers/answer', Answer, self._answersListener
        )

    def _answersListener(self, data):
        if self._answer_subscriber_state:
            self._robot_answer = data.replica.text
            self._answer_subscriber_state = False

    def getAnswer(self):
        rospy.sleep(self._timeout)
        return self._robot_answer.decode('utf-8')

    def cancelSpeechPub(self):
        self._pub_cancel_speech.publish()
        rospy.sleep(self._timeout)

    def ttsPub(self, data):
        tts_command = TTSCommand()
        tts_command.text = data.text
        tts_command.terminate = False
        tts_command.uuid = data.uuid
        tts_command.ignore_saving = False
        self._pub_text_to_tts.publish(tts_command)
        rospy.sleep(self._timeout)

    def getLevelsOrder(self):
        return self._levels_order
