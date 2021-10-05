#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.unit
def test_asr(node):
    node.cancelSpeechPub()
    node.asrPub('нет')
    assert node.getAnswer() == 'тестовое правило с нет'


@pytest.mark.unit
def test_tts(node):
    node.cancelSpeechPub()
    node.ttsPub('я робот ты робот')
    assert node.getTts() == 'я робот ты робот'


@pytest.mark.unit
def test_levels_order(node):
    assert node.getLevelsOrder() == ['0', '1', '2', '3', '4', '5', '6', '7']


@pytest.mark.unit
def test_levels_service_set(node):
    node.setLevelSrv([0, 1, 3, 2, 7])
    assert node.getLevelSrv() == ['0', '1', '3', '2', '7']


@pytest.mark.unit
def test_levels_service_reset(node):
    node.resetLevelSrv()
    assert node.getLevelSrv() == ['0', '1', '2', '3', '4', '5', '6', '7']
