#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.test_config import modals_timeout
'''
26.21 seconds
'''


@pytest.mark.interface_connection_modals
def test_connection_open(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('connection')
    time.sleep(modals_timeout)
    assert screenDiffChecker('connection.png', (0, 40, 920, 150)) is None


@pytest.mark.interface_connection_modals
def test_connection_info_modal(clickOn, screenDiffChecker):
    clickOn('connection_info')
    time.sleep(modals_timeout)
    assert screenDiffChecker(
        'connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.interface_connection_modals
def test_connection_update_modal(clickOn, screenDiffChecker):
    clickOn('connection_info_modal_close')
    clickOn('connection_update')
    time.sleep(2)
    assert screenDiffChecker(
        'connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.interface_connection_modals
def test_connection_wifi_pass_modal(clickOn, screenDiffChecker):
    time.sleep(modals_timeout)
    clickOn('random_wifi')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker(
        'wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.interface_connection_modals
def test_reset(clickOn, screenDiffChecker):
    clickOn('wifi_pass_modal_close')
    clickOn('back')
    clickOn('back')
    time.sleep(modals_timeout)
