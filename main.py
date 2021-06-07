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


class AutoTest:
    def __init__(self):
        # публикатор текста для распознавания речи
        self.pub_text_to_asr = rospy.Publisher(
            'asr/result', ASRResult, queue_size=10)
        # публикатор текста на произношение
        self.pub_text_to_tts = rospy.Publisher(
            'tts/start', TTSCommand, queue_size=10)
        # публикатор прерывания текущего произношения
        self.pub_cancel_speech = rospy.Publisher(
            'tts/cancel', Empty, queue_size=10)
        # публикатор лица для распознавания лиц
        self.pub_face_to_faceArray = rospy.Publisher(
            'face/info/array', FaceArray, queue_size=10)
        # публикатор переключение режима езды
        self.pub_drive_mode = rospy.Publisher(
            'drive/mode', UInt16, queue_size=10)
        # публикатор отправки робота на точку в навигации
        self.pub_drive_to_point = rospy.Publisher(
            'drive/point', UInt16, queue_size=10)

        # переменная для подписчика
        self.answer_subscriber_state = False
        # переменная для записи ответа
        self.robot_answer = ''
        # таймауты
        self.timeout = 0.5

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
        self.pub_text_to_asr.publish(asr_result)
        time.sleep(self.timeout)

    # метод оправки текста на произношение
    def ttsPub(self, values):
        tts_command = TTSCommand()
        tts_command.text = values.text
        tts_command.terminate = False
        tts_command.uuid = values.uuid
        tts_command.ignore_saving = False
        tts_command.rate = 0
        self.pub_text_to_tts.publish(tts_command)
        time.sleep(self.timeout)

    # подписчик для получения ответа робота
    def answersListner(self):
        self.robot_answer = ''
        self.answer_subscriber_state = True
        time.sleep(self.timeout)
        rospy.Subscriber('answers/answer', Answer,
                        self._answersListnerCallback)

    # callback для получения значения переменной ответа
    def _answersListnerCallback(self, data):
        if self.answer_subscriber_state:
            self.robot_answer = data.replica.text
            self.answer_subscriber_state = False

    # метод прерывания текущей реплики робота
    def cancelSpeech(self):
        self.pub_cancel_speech.publish()
        time.sleep(self.timeout)

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
        self.pub_face_to_faceArray.publish(face_array)
        time.sleep(self.timeout)

    # метод для активации режима "авто"
    def autoModePub(self):
        self.pub_drive_mode.publish(1)
        time.sleep(self.timeout)

    # метод для активации режима "джойстик"
    def joyModePub(self):
        self.pub_drive_mode.publish(0)
        time.sleep(self.timeout)

    # метод для отправки робота на точку
    def driveToPointPub(self, values):
        self.pub_drive_to_point.publish(values.point)
        time.sleep(self.timeout)

    def getAnswer(self):
        time.sleep(self.timeout)
        return self.robot_answer.decode('utf-8')


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
