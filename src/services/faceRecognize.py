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

        self._fr_timeout = 0.5

    def facePub(self, data):
        face_array = FaceArray()
        face = Face()
        face_score = FaceScore()
        face.type = data.type
        face.source = 1
        face.is_tracking = data.is_tracking
        face.track_id = data.track_id
        face.id = data.id
        face.gender = 0
        face.age = 0.0
        face.emotion = ''
        face.liveness_type = 0
        face_score.source = 3
        face_score.personSource = 1
        face_score.id = data.id
        face_score.score = data.score
        face.persons = [face_score]
        # чистим массив лиц перед отправкой
        face_array.faces = []
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._fr_timeout)
        # публикуем нужное лицо
        face_array.faces.append(face)
        self._pub_face_to_faceArray.publish(face_array)
        rospy.sleep(self._fr_timeout)
