#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class InteractionParameters(enum.Enum):
    startBySpeech = (1119, 201)
    startBySpeechEnable = (893, 253)
    startBySpeechDisable = (914, 146)
    updateBySpeech = (1119, 453)
    updateBySpeechEnable = (900, 501)
    updateBySpeechDisable = (894, 400)
    startByFace = (1117, 389)
    startByFaceEnable = (919, 447)
    startByFaceDisable = (907, 352)
    updateByFace = (1123, 529)
    updateByFaceEnable = (936, 583)
    updateByFaceDisable = (922, 485)
