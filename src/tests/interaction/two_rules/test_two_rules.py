#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import interaction
from src.helpers.messages import InteractionMsg, AsrTtsMsg
'''
X seconds
'''


@pytest.mark.interaction_two_rules
def test_start_interaction(node):
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_two_rules
def test_two_rules(node, screenDiffChecker):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('давай другую руку')
    node.asrPub(asr_msg)
    assert screenDiffChecker(
        'interaction/two_rules.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interaction_two_rules
def test_first_rule(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('давай руку')
    node.asrPub(asr_msg)
    assert node.getScriptProcess() == ['get_hand_boy', True]


@pytest.mark.interaction_two_rules
def test_second_rule(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('давай другую руку')
    node.asrPub(asr_msg)
    node.cancelSpeechPub()
    node.cancelScriptPub()
    asr_msg = AsrTtsMsg('другую руку')
    node.asrPub(asr_msg)
    assert node.getScriptProcess() == ['get_hand_boy_dr', True]


@pytest.mark.interaction_two_rules
def test_reset(node):
    node.cancelSpeechPub()
    node.cancelScriptPub()
    time.sleep(interaction)
