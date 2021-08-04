#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import time

from promobot_msgs.msg import ASRResult
from promobot_msgs.msg import Answer
from promobot_msgs.msg import FaceArray
from promobot_msgs.msg import Face
from promobot_msgs.msg import FaceScore
from promobot_msgs.msg import TTSCommand
from promobot_msgs.msg import Interaction
from sensor_msgs.msg import Joy
from std_msgs.msg import Empty
from std_msgs.msg import UInt16
from std_msgs.msg import Bool
from std_msgs.msg import String
from std_msgs.msg import Empty
from std_msgs.msg import Int32


class AutoTest:
    def __init__(self):
        ''' 
        publishers для asr / tts
        '''
        self._pub_text_to_asr = rospy.Publisher(
            'asr/result', ASRResult, queue_size=10
        )
        self._pub_text_to_tts = rospy.Publisher(
            'tts/start', TTSCommand, queue_size=10
        )
        self._pub_cancel_speech = rospy.Publisher(
            'tts/cancel', Empty, queue_size=10
        )
        '''
        publishers для faceRecognize
        '''
        self._pub_face_to_faceArray = rospy.Publisher(
            'face/info/array', FaceArray, queue_size=10
        )
        '''
        publishers для drive
        '''
        self._pub_drive_mode = rospy.Publisher(
            'drive/mode', UInt16, queue_size=10
        )

        self._pub_drive_to_point = rospy.Publisher(
            'drive/point', UInt16, queue_size=10
        )
        '''
        publishers для joy
        '''
        self._pub_joy_phrase_mode = rospy.Publisher(
            'joy/speech/switch', Empty, queue_size=10
        )

        self._pub_joy_cmd = rospy.Publisher('joy', Joy, queue_size=10)

        '''
        publishers для interaction
        '''
        self._pub_interaction = rospy.Publisher(
            'interaction', Interaction, queue_size=10
        )
        '''
        subscribers
        '''
        rospy.Subscriber(
            'answers/answer', Answer, self._answersListenerCallback
        )
        rospy.Subscriber(
            'interaction', Interaction, self._interactionListenerCallback
        )
        rospy.Subscriber(
            'rwheel', Int32, self._rwheelListenerCallback
        )
        rospy.Subscriber(
            'lwheel', Int32, self._lwheelListenerCallback
        )
        rospy.Subscriber(
            'drive/point', UInt16, self._pointListenerCallback
        )
        '''
        Переменные subscribers
        '''
        self._answer_subscriber_state = False
        self._interaction_subscriber_state = False
        '''
        Переменные для getters
        '''
        self._robot_answer = ''
        self._interaction_state = ''
        self._interaction_reason = ''
        self._rwheel_data = ''
        self._lwheel_data = ''
        self._current_point = ''

        '''
        sleep for publishers
        '''
        self._timeout = 0.5

    ''' 
    методы для asr / tts
    '''

    def asrPub(self, values):
        asr_result = ASRResult()
        asr_result.header.frame_id = "asr"
        asr_result.header.stamp = rospy.get_rostime()
        asr_result.source = 0
        asr_result.uuid = values.uuid
        asr_result.text = values.text
        asr_result.final = 1
        asr_result.conf = 1.0
        self._pub_text_to_asr.publish(asr_result)
        rospy.sleep(self._timeout)

    def ttsPub(self, values):
        tts_command = TTSCommand()
        tts_command.text = values.text
        tts_command.terminate = False
        tts_command.uuid = values.uuid
        tts_command.ignore_saving = False
        tts_command.rate = 0
        self._pub_text_to_tts.publish(tts_command)
        rospy.sleep(self._timeout)

    def answersListener(self):
        self._robot_answer = ''
        self._answer_subscriber_state = True
        rospy.sleep(self._timeout)

    def _answersListenerCallback(self, data):
        if self._answer_subscriber_state:
            self._robot_answer = data.replica.text
            self._answer_subscriber_state = False

    def cancelSpeech(self):
        self._pub_cancel_speech.publish()
        rospy.sleep(self._timeout)

    def getAnswer(self):
        rospy.sleep(self._timeout)
        return self._robot_answer.decode('utf-8')

    ''' 
    методы для faceRecognize
    '''

    def facePub(self, values):
        face_array = FaceArray()
        face = Face()
        face_score = FaceScore()
        face.type = values.type
        face.source = 1
        face.is_tracking = True
        face.track_id = 10
        face.id = values.id
        face.gender = 0
        face.age = 0.0
        face.emotion = ''
        face.facemask = values.facemask
        face.is_fake = False
        face_score.source = 3
        face_score.personSource = 1
        face_score.id = values.id
        face_score.score = values.score
        face.persons = [face_score]
        face_array.faces.append(face)
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)

    '''
    методы для driving
    '''

    def autoModePub(self):
        self._pub_drive_mode.publish(1)
        rospy.sleep(self._timeout)

    def joyModePub(self):
        self._pub_drive_mode.publish(0)
        rospy.sleep(self._timeout)

    def driveToPointPub(self, values):
        self._pub_drive_to_point.publish(values.point)
        rospy.sleep(self._timeout)

    def _rwheelListenerCallback(self, data):
        self._rwheel_data = data

    def _lwheelListenerCallback(self, data):
        self._lwheel_data = data

    def _pointListenerCallback(self, data):
        self._current_point = data

    def getWheelsData(self):
        return [self._rwheel_data, self._rwheel_data]
    '''
    методы для joy
    '''

    def switchJoyPhraseMode(self):
        self._pub_joy_phrase_mode.publish()
        rospy.sleep(self._timeout)

    def sendJoyCommand(self, values):
        joy = Joy()
        joy.header.frame_id = ''
        joy.header.stamp = rospy.get_rostime()
        '''
        axes и buttons представляют собой массив float и int, сообщение формируется отдельным классом: JoyCmdMsg().
        Добавлены команды: upVolume, downVolume, upMic, downMic, phraseMode, nextPhrase, previosePhrase, autoMode
        чтобы сформировать сообщение, необходимо вызвать нужный метод. Пример:
        joy = JoyCmdMsg()
        joy_msg = joy.autoMode()
        '''
        joy.axes = values['axes']
        joy.buttons = values['buttons']
        self._pub_joy_cmd.publish(joy)
        rospy.sleep(self._timeout)

    '''
    методы для interaction
    '''

    def startInteraction(self, values):
        interaction = Interaction()
        interaction.state = values.state
        interaction.reason = values.reason
        self._pub_interaction.publish(interaction)
        rospy.sleep(self._timeout)

    def interactionListener(self):
        self._interaction_subscriber_state = True
        rospy.sleep(self._timeout)

    def _interactionListenerCallback(self, data):
        if self._interaction_subscriber_state:
            self._interaction_state = data.state
            self._interaction_reason = data.reason
            self._interaction_subscriber_state = False

    def getInteraction(self):
        return [self._interaction_state, self._interaction_reason]
