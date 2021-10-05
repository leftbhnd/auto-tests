#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import interaction
'''
X seconds
'''


@pytest.mark.interaction_levels
def test_robot_base(node):
    node.asrPub('порядок')
    assert node.getAnswer() == 'Робот высокий приоритет'


@pytest.mark.interaction_levels
def test_owner_base(node):
    node.cancelSpeechPub()
    node.setLevelSrv([1, 2, 3, 4, 5, 6, 7, 0])
    node.asrPub('порядок')
    assert node.getAnswer() == 'Владелец высокий приоритет'


@pytest.mark.interaction_levels
def test_robot_base_low(node):
    node.cancelSpeechPub()
    node.setLevelSrv([2, 3, 4, 5, 6, 7, 0, 1])
    node.asrPub('порядок')
    assert node.getAnswer() == 'Робот низкий приоритет'


@pytest.mark.interaction_levels
def test_owner_base_low(node):
    node.cancelSpeechPub()
    node.setLevelSrv([3, 4, 5, 6, 7, 0, 1, 2])
    node.asrPub('порядок')
    assert node.getAnswer() == 'Владелец низкий приоритет'


@pytest.mark.interaction_levels
def test_common_base(node):
    node.cancelSpeechPub()
    node.setLevelSrv([4, 5, 6, 7, 0, 1, 2, 3])
    node.asrPub('порядок')
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_internet_base(node):
    node.cancelSpeechPub()
    node.setLevelSrv([5, 6, 7, 0, 1, 2, 3, 4])
    node.asrPub('порядок')
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_common_base_low(node):
    node.cancelSpeechPub()
    node.setLevelSrv([6, 7, 0, 1, 2, 3, 4, 5])
    node.asrPub('порядок')
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_unrecognized(node):
    node.cancelSpeechPub()
    node.setLevelSrv([7, 0, 1, 2, 3, 4, 5, 6])
    node.asrPub('порядок')
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_restore(node):
    node.cancelSpeechPub()
    node.resetLevelSrv()
    time.sleep(interaction)
    assert node.getLevelSrv() == ['0', '1', '2', '3', '4', '5', '6', '7']
