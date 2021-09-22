#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import interaction
from src.test_data.interaction import surprises
'''
24.44 seconds
'''

answer = ''

@pytest.mark.interaction_surprises
def test_start_interaction(node):
    node.interactionPub(True, 0)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_surprises
def test_first_surprise(node):
    node.cancelSpeechPub()
    node.asrPub('удиви меня')
    answer = node.getAnswer()
    assert answer in surprises


@pytest.mark.interaction_surprises
def test_second_surprise(node):
    node.cancelSpeechPub()
    node.asrPub('удиви меня')
    assert ((node.getAnswer() in surprises) and (answer != node.getAnswer()))


@pytest.mark.interaction_surprises
def test_restore(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
