#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import resetAnchor, interaction
'''
42.76 seconds
'''


@pytest.mark.interaction_anchor
def test_start_interaction(node):
    node.interactionPub(True, 0)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_anchor
def test_anchor(node):
    node.cancelSpeechPub()
    node.asrPub('спой гимн')
    assert node.getAnswer() == 'Вы хотите, чтобы я спел?'


@pytest.mark.interaction_anchor
def test_anchor_yes(node):
    node.cancelSpeechPub()
    node.asrPub('да')
    assert node.getAnswer() == 'хорошо'


@pytest.mark.interaction_anchor
def test_anchor_no(node):
    node.cancelSpeechPub()
    node.asrPub('спой гимн')
    node.cancelSpeechPub()
    node.asrPub('нет')
    assert node.getAnswer() == 'нет так нет'


@pytest.mark.interaction_anchor
def test_check_reset_anchor(node):
    node.cancelSpeechPub()
    node.asrPub('спой гимн')
    node.cancelSpeechPub()
    time.sleep(resetAnchor)
    node.asrPub('нет')
    assert node.getAnswer() == 'тестовое правило с нет'


@pytest.mark.interaction_anchor
def test_reset(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
