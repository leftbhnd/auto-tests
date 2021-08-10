#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy


from src.modules.driving import DrivingService
from src.modules.faceRecognize import FaceRecognizeService
from src.modules.interaction import InteractionService
from src.modules.joy import JoyService
from src.modules.script import ScriptService
from src.modules.servos import ServosService
from src.modules.ttsAsr import TtsAsrService


class AutoTest(DrivingService, FaceRecognizeService, InteractionService, JoyService, ScriptService, ServosService, TtsAsrService):
    def __init__(self):
        DrivingService.__init__(self)
        FaceRecognizeService.__init__(self)
        InteractionService.__init__(self)
        JoyService.__init__(self)
        ScriptService.__init__(self)
        ServosService.__init__(self)
        TtsAsrService.__init__(self)
