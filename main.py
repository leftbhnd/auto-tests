#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy


from src.modules.driving import Driving
from src.modules.faceRecognize import FaceRecognize
from src.modules.interaction import Interaction
from src.modules.joy import Joy
from src.modules.script import Script
from src.modules.servos import Servos
from src.modules.ttsAsr import TtsAsr


class AutoTest(Driving, FaceRecognize, Interaction, Joy, Script, Servos, TtsAsr):
    def __init__(self):
        Driving.__init__(self)
        FaceRecognize.__init__(self)
        Interaction.__init__(self)
        Joy.__init__(self)
        Script.__init__(self)
        Servos.__init__(self)
        TtsAsr.__init__(self)
