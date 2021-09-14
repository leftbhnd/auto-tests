#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import resetAnchor, interaction
from src.helpers.messages import InteractionMsg, AsrTtsMsg
'''
X seconds
'''


@pytest.mark.interaction_anchor
def test_start_interaction(node):
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_anchor
def test_anchor(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('спой гимн')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'Вы хотите, чтобы я спел?'


@pytest.mark.interaction_anchor
def test_anchor_yes(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('да')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'хорошо'


@pytest.mark.interaction_anchor
def test_anchor_no(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('спой гимн')
    node.asrPub(asr_msg)
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('нет')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'нет так нет'


@pytest.mark.interaction_anchor
def test_check_reset_anchor(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('спой гимн')
    node.asrPub(asr_msg)
    node.cancelSpeechPub()
    time.sleep(resetAnchor)
    asr_msg = AsrTtsMsg('нет')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'тестовое правило с нет'


@pytest.mark.interaction_anchor
def test_reset(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
