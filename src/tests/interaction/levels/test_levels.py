#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, running, restart
'''
750 seconds
'''

@pytest.fixture
def changeLevel(click, dNd, openServiceMenu):
    def _method():
        openServiceMenu()
        click(btn.control.settings)
        click(btn.settings.lingvo)
        click(btn.lingvo.sources)
        click(btn.lingvo.first_level)
        dNd((446, 233), (446, 655))
        click(btn.handler.back)
        click(modal.save.yes)
        time.sleep(modals)
        click(btn.handler.back)
        click(btn.control.restart)
        click(modal.restart.yes)
        time.sleep(restart)
        click(btn.start.play)
        click(modal.radius.yes)
        time.sleep(running)
    return _method


@pytest.mark.interaction_levels
def test_robot_base(node):
    node.asrPub('порядок')
    assert node.getAnswer() == 'Робот высокий приоритет'


@pytest.mark.interaction_levels
def test_owner_base(changeLevel, node):
    changeLevel()
    node.asrPub('порядок')
    assert node.getAnswer() == 'Владелец высокий приоритет'


@pytest.mark.interaction_levels
def test_robot_base_low(changeLevel, node):
    changeLevel()
    node.asrPub('порядок')
    assert node.getAnswer() == 'Робот низкий приоритет'


@pytest.mark.interaction_levels
def test_owner_base_low(changeLevel, node):
    changeLevel()
    node.asrPub('порядок')
    assert node.getAnswer() == 'Владелец низкий приоритет'


@pytest.mark.interaction_levels
def test_common_base(changeLevel, node):
    changeLevel()
    node.asrPub('порядок')
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_internet_base(changeLevel, node):
    changeLevel()
    node.asrPub('порядок')
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_common_base_low(changeLevel, node):
    changeLevel()
    node.asrPub('порядок')
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_unrecognized(changeLevel, node):
    changeLevel()
    node.asrPub('порядок')
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_restore(changeLevel, node):
    changeLevel()
    assert node.getLevelsOrder() == ['0', '1', '2', '3', '4', '5', '6', '7']
