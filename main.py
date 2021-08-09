#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy

from driving import Driving
from faceRecognize import FaceRecognize
from interaction import Interaction
from joy import Joy
from script import Script
from servos import Servos
from ttsAsr import TtsAsr


class AutoTest(Driving, FaceRecognize, Interaction, Joy, Script, Servos, TtsAsr):
    def __init__(self):
        Driving.__init__(self)
        FaceRecognize.__init__(self)
        Interaction.__init__(self)
        Joy.__init__(self)
        Script.__init__(self)
        Servos.__init__(self)
        TtsAsr.__init__(self)
