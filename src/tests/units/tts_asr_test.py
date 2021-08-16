#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import pytest
import time

from src.helpers.messages import AsrTtsMsg


def test_asr(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('привет', '1143c011-a2a4-12eb-bcbc-0242ac132200')
    node.asrPub(asr_msg)
    node.answersListener()
    assert node.getAnswer() in [
        "Доброго времени суток!",
        "Доброго времени суток! Добро пожаловать в {company}.",
        "Приветики! Добро пожаловать в {company}.",
        "И вам привет! Как поживаете?",
        "Какая честь! Как поживаете?",
        "Приветики! Как поживаете?",
        "Приветики!"
    ]


def test_tts(node):
    time.sleep(10)
    node.cancelSpeechPub()
    tts_msg = AsrTtsMsg('я робот ты робот',
                        '11520092-a2a7-13eb-bcbc-0242ac132222')
    node.ttsPub(tts_msg)
    node.ttsListener()
    assert node.getTts() == 'я робот ты робот'


def test_levels_order(node):
    assert node.getLevelsOrder() == ['0', '1', '2', '3', '4', '5', '6', '7']
