#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.testConfig import running_timeout, restart_timeout
'''
X seconds
'''


@pytest.mark.interaction
def test_activate_phrase_mode(clickOn, joy, node, screenDiffChecker):
    clickOn('play')
    clickOn('radius_modal_yes')
    time.sleep(running_timeout)
    joy_msg = joy.phraseMode()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker('interfaces/joy_mode_on', (0, 40, 1280, 660)) is None


@pytest.mark.interaction
def test_first_phrase(joy, node):
    joy_msg = joy.nextPhrase()
    node.joyCommandPub(joy_msg)
    assert node.getTts() is 'тестовая фраза 1'


@pytest.mark.interaction
def test_second_phrase(joy, node):
    joy_msg = joy.nextPhrase()
    node.joyCommandPub(joy_msg)
    assert node.getTts() == 'тестовая фраза 2'


@pytest.mark.interaction
def test_previous_phrase(joy, node):
    joy_msg = joy.previousPhrase()
    node.joyCommandPub(joy_msg)
    assert node.getTts() == 'тестовая фраза 1'


@pytest.mark.interaction
def test_reset(clickOn, typeText, openPasswordModal, screenDiffChecker):
    openPasswordModal()
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(restart_timeout)
    assert screenDiffChecker('interfaces/start.png') is None
