#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.test_config import modals_timeout
'''
17.66 seconds
'''


@pytest.mark.interface
def test_connection_open(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('connection')
    time.sleep(modals_timeout)
    screenDiffChecker('connection.png', (0, 40, 920, 150)) is None


@pytest.mark.interface
def test_hide_input(clickOn, typeText, screenDiffChecker):
    time.sleep(modals_timeout)
    clickOn('random_wifi')
    clickOn('wifi_pass_modal_input')
    clickOn('choose_numbers')
    typeText('2281488')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker(
        'wifi_hide_pass.png',
        (365, 162, 548, 200)
    ) is None


@pytest.mark.interface
def test_visiable_input(clickOn, screenDiffChecker):
    clickOn('kb_wifi_pass_modal_eye')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker(
        'wifi_visiable_pass.png',
        (365, 162, 548, 200)
    ) is None


@pytest.mark.interface
def test_reset(clickOn, screenDiffChecker):
    clickOn('kb_wifi_pass_modal_close')
    clickOn('back')
    clickOn('back')
    time.sleep(modals_timeout)
