#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import interaction
from src.test_data.interaction import jokes
'''
24.52 seconds
'''

answer = ''

@pytest.mark.interaction_jokes
def test_start_interaction(node):
    node.interactionPub(True, 0)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_jokes
def test_first_joke(node):
    node.cancelSpeechPub()
    node.asrPub('расскажи анекдот')
    answer = node.getAnswer()
    assert answer in jokes


@pytest.mark.interaction_jokes
def test_second_joke(node):
    node.cancelSpeechPub()
    node.asrPub('расскажи анекдот')
    assert ((node.getAnswer() in jokes) and (answer != node.getAnswer()))


@pytest.mark.interaction_jokes
def test_restore(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
