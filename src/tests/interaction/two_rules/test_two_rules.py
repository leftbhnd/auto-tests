#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import interaction
'''
28.11 seconds
'''


@pytest.mark.interaction_two_rules
def test_two_rules(node, screenDiffChecker):
    node.cancelSpeechPub()
    node.asrPub('давай другую руку')
    assert screenDiffChecker(
        'interaction/two_rules.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interaction_two_rules
def test_first_rule(node):
    node.cancelSpeechPub()
    node.asrPub('давай руку')
    assert node.getScriptProcess() == [True, 'get_hand_boy']


@pytest.mark.interaction_two_rules
def test_second_rule(node):
    node.cancelSpeechPub()
    node.asrPub('давай другую руку')
    node.cancelSpeechPub()
    node.cancelScriptPub()
    node.asrPub('другую руку')
    assert node.getScriptProcess() == [True, 'get_hand_boy_dr']


@pytest.mark.interaction_two_rules
def test_reset(node):
    node.cancelSpeechPub()
    node.cancelScriptPub()
    time.sleep(interaction)
