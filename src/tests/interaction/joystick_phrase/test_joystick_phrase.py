#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import running, restart, btn, modal
'''
X seconds
'''


@pytest.mark.interaction
def test_activate_phrase_mode(clickOn, joy, node, screenDiffChecker):
    node.initNode()
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
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
def test_reset(node, clickOn, typeText, openPasswordModal, screenDiffChecker):
    node.killNode()
    openPasswordModal()
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    assert screenDiffChecker('interfaces/start.png') is None
