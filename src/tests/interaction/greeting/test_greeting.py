#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, param, interaction
'''
65.29 seconds
'''


@pytest.mark.interaction_greeting
def test_success_greeting_unknown_first(node):
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getTts() == 'тестовый привет, незнакомец'


@pytest.mark.interaction_greeting
def test_faild_greeting_unknown_second(node):
    node.clearFacePub()
    node.cancelSpeechPub()
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getTts() == ''


@pytest.mark.interaction_greeting
def test_success_greeting_known_first(node):
    node.clearFacePub()
    node.cancelSpeechPub()
    node.facePub(2, 1, 1632114331, 2, 0.9)
    assert node.getTts() == 'тестовый привет, ДМИТРИЙЙ'


# параметр кол-ва обращений по имени
@pytest.mark.interaction_greeting
def test_failed_greeting_known_second(node):
    node.clearFacePub()
    node.cancelSpeechPub()
    node.facePub(2, 1, 1632114331, 2, 0.9)
    assert node.getTts() == 'тестовый привет, ДМИТРИЙЙ'


@pytest.mark.interaction_greeting
def test_set_zero_greeting_timeout(click, openServiceMenu, node):
    node.clearFacePub()
    openServiceMenu()
    click(btn.control.settings)
    click(btn.settings.system)
    click(btn.system.dialog)
    click(btn.handler.dialog_down_arr)
    for i in range(5):
        click(param.dialog.timeRecently_decrease)
    for i in range(2):
        click(param.dialog.timeRecentlyUnknown_decrease)
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.reset)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.reset)


@pytest.mark.interaction_greeting
def test_first_greeting_unknown(node):
    node.cancelSpeechPub()
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getTts() == 'тестовый привет, незнакомец'


@pytest.mark.interaction_greeting
def test_second_greeting_unknown(node):
    node.clearFacePub()
    node.cancelSpeechPub()
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getTts() == 'тестовый привет, незнакомец'


@pytest.mark.interaction_greeting
def test_first_greeting_known(node):
    node.clearFacePub()
    node.cancelSpeechPub()
    node.facePub(2, 1, 1632114331, 2, 0.9)
    assert node.getTts() == 'тестовый привет, ДМИТРИЙЙ'


@pytest.mark.interaction_greeting
def test_second_greeting_known(node):
    node.clearFacePub()
    node.cancelSpeechPub()
    node.facePub(2, 1, 1632114331, 2, 0.9)
    assert node.getTts() == 'тестовый привет, ДМИТРИЙЙ'


@pytest.mark.interaction_greeting
def test_restore(click, openServiceMenu, node):
    node.clearFacePub()
    openServiceMenu()
    click(btn.control.settings)
    click(btn.settings.system)
    click(btn.system.dialog)
    click(btn.handler.dialog_down_arr)
    for i in range(5):
        click(param.dialog.timeRecently_increase)
    for i in range(2):
        click(param.dialog.timeRecentlyUnknown_increase)
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.reset)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(interaction)
