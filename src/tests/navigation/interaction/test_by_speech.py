#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly, interaction
'''
X seconds
'''


@pytest.mark.navigation_interaction
def test_start_speech_in_driving(node):
    node.autoModePub()
    while node.getDrivePause() != False:
        time.sleep(slowly)
    time.sleep(5)
    node.asrPub('привет')
    assert node.getInteraction() == [True, 1]


@pytest.mark.navigation_interaction
def test_update_speech_in_driving(node):
    time.sleep(10)
    in_interaction = node.getInteraction()
    node.asrPub('привет')
    time.sleep(10)
    assert node.getInteraction() == in_interaction


@pytest.mark.navigation_interaction
def test_speech_continue_driving(node):
    time.sleep(interaction - 10)
    assert node.getDrivePause() == False


@pytest.mark.navigation_interaction
def test_start_speech_at_point(node):
    while node.getCurrentPoint() != 1:
        time.sleep(slowly)
    node.asrPub('привет')
    assert node.getInteraction() == [True, 1]


@pytest.mark.navigation_interaction
def test_update_speech_at_point(node):
    time.sleep(10)
    in_interaction = node.getInteraction()
    node.asrPub('привет')
    time.sleep(10)
    assert node.getInteraction() == in_interaction


@pytest.mark.navigation_interaction
def test_reset(node):
    node.chargeAppPub()
    time.sleep(60)
    assert node.getChargeState() == True
