#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, interaction
'''
57.86 seconds
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
def test_set_zero_greeting_timeout(click, openServiceMenu, node, db):
    node.clearFacePub()
    db.updateValue([
        {'name': '/dialog/timeRecently', 'value': 0.0},
        {'name': '/dialog/timeRecentlyUnknown', 'value': 0.0}
    ])
    openServiceMenu()
    click(btn.handler.back)


@pytest.mark.interaction_greeting
def test_first_greeting_unknown(node):
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
def test_restore(click, openServiceMenu, node, db):
    node.clearFacePub()
    db.updateValue([
        {'name': '/dialog/timeRecently', 'value': 5.0},
        {'name': '/dialog/timeRecentlyUnknown', 'value': 2.0}
    ])
    openServiceMenu()
    click(btn.handler.back)
    time.sleep(interaction)
