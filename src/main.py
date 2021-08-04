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
from std_msgs.msg import Empty
from std_msgs.msg import UInt16
from std_msgs.msg import Bool
from std_msgs.msg import String
from std_msgs.msg import Empty


class AutoTest:
    def __init__(self):
        # публикатор текста для распознавания речи
        self._pub_text_to_asr = rospy.Publisher(
            'asr/result', ASRResult, queue_size=10
        )
        # публикатор текста на произношение
        self._pub_text_to_tts = rospy.Publisher(
            'tts/start', TTSCommand, queue_size=10
        )
        # публикатор прерывания текущего произношения
        self._pub_cancel_speech = rospy.Publisher(
            'tts/cancel', Empty, queue_size=10
        )
        # публикатор лица для распознавания лиц
        self._pub_face_to_faceArray = rospy.Publisher(
            'face/info/array', FaceArray, queue_size=10
        )
        # публикатор переключение режима езды
        self._pub_drive_mode = rospy.Publisher(
            'drive/mode', UInt16, queue_size=10
        )
        # публикатор отправки робота на точку в навигации
        self._pub_drive_to_point = rospy.Publisher(
            'drive/point', UInt16, queue_size=10
        )
        # публикатор переключения режима фраз с джойстика
        self._pub_joystick_phrase_mode = rospy.Publisher(
            'joy/speech/switch', Empty, queue_size=10
        )

        # переменная для подписчика
        self._answer_subscriber_state = False
        # переменная для записи ответа
        self._robot_answer = ''
        # таймауты
        self._timeout = 0.5

    # метод отправки сообщения в asr
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

    # метод оправки текста на произношение
    def ttsPub(self, values):
        tts_command = TTSCommand()
        tts_command.text = values.text
        tts_command.terminate = False
        tts_command.uuid = values.uuid
        tts_command.ignore_saving = False
        tts_command.rate = 0
        self._pub_text_to_tts.publish(tts_command)
        rospy.sleep(self._timeout)

    # подписчик для получения ответа робота
    def answersListner(self):
        self._robot_answer = ''
        self._answer_subscriber_state = True
        rospy.sleep(self._timeout)
        rospy.Subscriber(
            'answers/answer', Answer, self._answersListnerCallback
        )

    # callback для получения значения переменной ответа
    def _answersListnerCallback(self, data):
        if self._answer_subscriber_state:
            self._robot_answer = data.replica.text
            self._answer_subscriber_state = False

    # метод прерывания текущей реплики робота
    def cancelSpeech(self):
        self._pub_cancel_speech.publish()
        rospy.sleep(self._timeout)

    # метод отправки лица в распознавание речи
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

    # метод для активации режима "авто"
    def autoModePub(self):
        self._pub_drive_mode.publish(1)
        rospy.sleep(self._timeout)

    # метод для активации режима "джойстик"
    def joyModePub(self):
        self._pub_drive_mode.publish(0)
        rospy.sleep(self._timeout)

    # метод для отправки робота на точку
    def driveToPointPub(self, values):
        self._pub_drive_to_point.publish(values.point)
        rospy.sleep(self._timeout)

    # метод для переключения режима фраз с джойстик
    def switchJoystickPhraseMode(self):
        self._pub_joystick_phrase_mode.publish()
        rospy.sleep(self._timeout)

    def getAnswer(self):
        rospy.sleep(self._timeout)
        return self._robot_answer.decode('utf-8')


class AsrMsg:
    def __init__(self, text, uuid):
        self.text = text
        self.uuid = uuid


class ClickMsg:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class FaseMsg:
    def __init__(self, type, id, facemask, score):
        self.type = type
        self.id = id
        self.facemask = facemask
        self.score = score
