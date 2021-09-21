#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from promobot_msgs.msg import FaceArray
from promobot_msgs.msg import Face
from promobot_msgs.msg import FaceScore
#from src.helpers.messages import FaceMsg


class FaceRecognizeService:
    def __init__(self):
        '''
        publishers
        '''
        self._pub_face_to_faceArray = rospy.Publisher(
            'face/info/array', FaceArray, latch=True, queue_size=10
        )

        self._timeout = 0.5

    def facePub(self, type, is_tracking, track_id, id, source, score):
        face_array = FaceArray()
        face = Face()
        face_score = FaceScore()
        # чистим массив лиц перед отправкой
        face_array.faces = []
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)
        # имитируем нераспознанное лицо
        face.type = 1
        face.source = 1
        face.is_tracking = True
        face.track_id = 0
        face.id = -1
        face.gender = 0
        face.age = 0.0
        face.emotion = ''
        face.liveness_type = 0
        face_array.faces.append(face)
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)
        # публикуем нужное лицо
        face.type = type
        face.is_tracking = is_tracking
        face.track_id = track_id
        face.id = id
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
        face_array.faces.append(face)
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)
        face_array.faces = []
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._timeout)
