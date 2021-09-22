#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.unit
def test_asr(node):
    node.cancelSpeechPub()
    node.asrPub('привет')
    assert node.getAnswer() in [
        "Доброго времени суток!",
        "Доброго времени суток! Добро пожаловать в {company}.",
        "Приветики! Добро пожаловать в {company}.",
        "И вам привет! Как поживаете?",
        "Какая честь! Как поживаете?",
        "Приветики! Как поживаете?",
        "Приветики!"
    ]


@pytest.mark.unit
def test_tts(node):
    node.cancelSpeechPub()
    node.ttsPub('я робот ты робот')
    assert node.getTts() == 'я робот ты робот'


@pytest.mark.unit
def test_levels_order(node):
    assert node.getLevelsOrder() == ['0', '1', '2', '3', '4', '5', '6', '7']
