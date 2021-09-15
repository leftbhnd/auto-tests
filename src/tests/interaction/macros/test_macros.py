#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import interaction
from src.helpers.messages import InteractionMsg, AsrTtsMsg
'''
X seconds
TODO проверить, что отвечает
'''


@pytest.mark.interaction_macros
def test_start_interaction(node):
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    assert node.getInteraction()  == [True, 0]


@pytest.mark.interaction_macros
def test_first_macros(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('макрос')
    node.asrPub(asr_msg)
    assert node.getAnswer() == ''


@pytest.mark.interaction_macros
def test_second_macros(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('макрос')
    node.asrPub(asr_msg)
    assert node.getAnswer() == ''


@pytest.mark.interaction_macros
def test_third_macros(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('макрос')
    node.asrPub(asr_msg)
    assert node.getAnswer() == ''


@pytest.mark.interaction_macros
def test_restore(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
