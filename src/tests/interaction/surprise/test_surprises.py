#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import interaction
from src.helpers.messages import InteractionMsg, AsrTtsMsg
from src.test_data.interaction import surprises
'''
X seconds
'''

answer = ''

@pytest.mark.interaction_surprises
def test_start_interaction(node):
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_surprises
def test_first_joke(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('удиви меня')
    node.asrPub(asr_msg)
    answer = node.getAnswer()
    assert answer in surprises


@pytest.mark.interaction_surprises
def test_second_joke(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('удиви меня')
    node.asrPub(asr_msg)
    assert ((node.getAnswer() in surprises) and (answer != node.getAnswer()))


@pytest.mark.interaction_surprises
def test_restore(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
