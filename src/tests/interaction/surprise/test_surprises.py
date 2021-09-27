#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import interaction
from src.test_data.interaction import surprises
'''
23.18 seconds
'''

answer = ''


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
