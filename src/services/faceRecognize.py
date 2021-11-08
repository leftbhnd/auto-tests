#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import FaceArray
from promobot_msgs.msg import Face
from promobot_msgs.msg import FaceScore


class FaceRecognizeService:
    def __init__(self):
        '''
        publishers
        '''
        self._pub_face_to_faceArray = rospy.Publisher(
            'face/info/array', FaceArray, latch=True, queue_size=10
        )
        '''
        subscribers
        '''
        rospy.Subscriber(
            'face/info/array', FaceArray, self._faceInfoListener
        )
        '''
        переменные для геттеров
        '''
        self._face_type = 0

        self._timeout = 0.5

    def facePub(self, type, track_id, id, source, score):
        face_array = FaceArray()
        face = Face()
        face_score = FaceScore()
        # публикуем нужное лицо
        face.type = type
        face.source = source
        face.is_tracking = True
        face.track_id = track_id
        face.id = id
        face.gender = 0
        face.age = 0.0
        face.emotion = ''
        face.liveness_type = 0
        face_score.source = source
        face_score.personSource = 1
        face_score.id = id
        face_score.score = score
        face.persons = [face_score]
        face_array.faces.append(face)
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)

    def clearFacePub(self):
        face_array = FaceArray()
        face = Face()
        # имитируем лицо, вышедшее из кадра
        face.type = 0
        face.source = 1
        face.is_tracking = False
        face.track_id = 0
        face.id = -2
        face.gender = 0
        face.age = 0.0
        face.emotion = ''
        face.liveness_type = 0
        face.persons = []
        face_array.faces.append(face)
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)

    def _faceInfoListener(self, face_info):
        # [-1] последнее (актуальное) лицо в массиве с лицами
        face = face_info.faces[-1]
        # type = 1 - распознается / 2 - знаком / 3 - временная база
        self._face_type = face.type
        # можно дополнить и добавить для других ключей топика /face/info/array

    def getFaceIsAcquainted(self):
        if self._face_type == 2:
            return True
        else:
            return False
