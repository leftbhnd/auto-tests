#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class InteractionParams(enum.Enum):
    startByFace = '/interaction/startByFace'
    updateByFace = '/interaction/updateByFace'
    startBySpeech = '/interaction/startBySpeech'
    updateBySpeech = '/interaction/updateBySpeech'
    startByFaceInDrive = '/interaction/startByFaceInDrive'
    updateByFaceInDrive = '/interaction/updateByFaceInDrive'
    startBySpeechInDrive = '/interaction/startBySpeechInDrive'
    updateBySpeechInDrive = '/interaction/updateBySpeechInDrive'
