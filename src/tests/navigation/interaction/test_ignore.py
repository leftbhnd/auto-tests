#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, param, modal, slowly, restart, running
'''
X seconds
'''


@pytest.mark.navigation_interaction
def test_setup_ingore_interaction(click, openServiceMenu, node, db):
    db.updateValue([
        {'name': param.navigation.ignoreInteractions, 'value': True}
    ])
    openServiceMenu()
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    click(btn.start.play)
    time.sleep(running)
    node.autoModePub()
    assert node.getAnswer() == 'Еду на первую точку'


@pytest.mark.navigation_interaction
def test_start_speech_in_driving(node):
    while node.getDrivePause() != False:
        time.sleep(slowly)
    node.cancelSpeechPub()
    node.asrPub('привет')
    assert node.getAnswer() == 'Извините, я нахожусь в движение'


@pytest.mark.navigation_interaction
def test_ignore_speech_in_driving(node):
    node.cancelSpeechPub()
    assert node.getInteraction() == [False, 2]


@pytest.mark.navigation_interaction
def test_start_face_in_driving(node):
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getAnswer() == 'Извините, я нахожусь в движение'


@pytest.mark.navigation_interaction
def test_ignore_face_in_driving(node):
    node.clearFacePub()
    node.cancelSpeechPub()
    assert node.getInteraction() == [False, 2]


@pytest.mark.navigation_interaction
def test_start_click_in_driving(click, node):
    click(btn.handler.reset)
    assert node.getAnswer() == 'Извините, я нахожусь в движение'


@pytest.mark.navigation_interaction
def test_ignore_click_in_driving(node):
    node.cancelSpeechPub()
    assert node.getInteraction() == [False, 2]


@pytest.mark.navigation_interaction
def test_check_interaction_at_point(node):
    while node.getCurrentPoint() != 1:
        time.sleep(slowly)
    node.cancelSpeechPub()
    node.asrPub('привет')
    assert node.getInteraction() == [True, 0]


@pytest.mark.navigation_interaction
def test_reset(node):
    node.chargeAppPub()
    time.sleep(60)
    assert node.getChargeState() == True
