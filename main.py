#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy


from src.services.driving import DrivingService
from src.services.faceRecognize import FaceRecognizeService
from src.services.interaction import InteractionService
from src.services.joy import JoyService
from src.services.script import ScriptService
from src.services.servos import ServosService
from src.services.ttsAsr import TtsAsrService


class AutoTest(DrivingService, FaceRecognizeService, InteractionService, JoyService, ScriptService, ServosService, TtsAsrService):
    def __init__(self):
        DrivingService.__init__(self)
        FaceRecognizeService.__init__(self)
        InteractionService.__init__(self)
        JoyService.__init__(self)
        ScriptService.__init__(self)
        ServosService.__init__(self)
        TtsAsrService.__init__(self)
