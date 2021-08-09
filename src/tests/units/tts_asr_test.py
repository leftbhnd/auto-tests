#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import pytest

from src.helpers.messages import AsrTtsMsg


def test_asr(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('привет', '11520092-a2a4-12eb-bcbc-0242ac132200')
    node.asrPub(asr_msg)
    node.answersListener()
    assert node.getAnswer() is 'привет'


def test_tts(node):
    tts_msg = AsrTtsMsg('я робот ты робот',
                        '11520092-a2a4-12eb-bcbc-0242ac132222')
    node.ttsPub(tts_msg)


def test_levels_order(node):
    assert node.getLevelsOrder() == ['0', '1', '2', '3', '4', '5', '6', '7']
