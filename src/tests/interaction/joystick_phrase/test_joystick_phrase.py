#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import restart, btn, modal
'''
X seconds
'''


@pytest.mark.interaction_joy_phrase
def test_activate_phrase_mode(joy, node):
    node.initNode()
    joy_msg = joy.phraseMode()
    node.joyCommandPub(joy_msg)
    assert node.getJoySpeech() == True


@pytest.mark.interaction_joy_phrase
def test_first_phrase(joy, node):
    joy_msg = joy.nextPhrase()
    node.joyCommandPub(joy_msg)
    assert node.getTts() == 'тестовая фраза 1'


@pytest.mark.interaction_joy_phrase
def test_second_phrase(joy, node):
    joy_msg = joy.nextPhrase()
    node.joyCommandPub(joy_msg)
    assert node.getTts() == 'тестовая фраза 2'


@pytest.mark.interaction_joy_phrase
def test_previous_phrase(joy, node):
    joy_msg = joy.previousPhrase()
    node.joyCommandPub(joy_msg)
    assert node.getTts() == 'тестовая фраза 1'


@pytest.mark.interaction_joy_phrase
def test_reset(node, joy):
    joy_msg = joy.phraseMode()
    node.joyCommandPub(joy_msg)
    node.killNode()
    assert node.getJoySpeech() == False
