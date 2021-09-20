#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class RobotParams(enum.Enum):
    # driving
    useRadius = (1016, 205)
    inv_useRadius = (260, 194)
    # dialog
    [{'u_i': (1117, 616)}, {'u_d': (895, 619)}, {'k_i': (1117, 668)}, {'k_d': (893, 667)}]

    timeRecently_increase = (1117, 668)
    timeRecently_decrease = (893, 667)
    timeRecentlyUnknown_increase = (1117, 616)
    timeRecentlyUnknown_decrease = (895, 619)
    # interaction
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
