#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import interaction
from src.test_data.interaction import macroses
'''
28.30 seconds
'''


@pytest.mark.interaction_macros
def test_first_macros(node):
    node.cancelSpeechPub()
    node.asrPub('макрос')
    assert node.getAnswer() in macroses


@pytest.mark.interaction_macros
def test_second_macros(node):
    node.cancelSpeechPub()
    node.asrPub('макрос')
    assert node.getAnswer() in macroses


@pytest.mark.interaction_macros
def test_third_macros(node):
    node.cancelSpeechPub()
    node.asrPub('макрос')
    assert node.getAnswer() in macroses


@pytest.mark.interaction_macros
def test_fourth_macros(node):
    node.cancelSpeechPub()
    node.asrPub('макрос')
    assert node.getAnswer() in macroses


@pytest.mark.interaction_macros
def test_restore(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
