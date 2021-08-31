#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
26.21 seconds
'''


@pytest.mark.interface_connection_modals
def test_connection_open(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.interface_connection_modals
def test_connection_info_modal(clickOn, screenDiffChecker):
    clickOn(btn.connection_info)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.interface_connection_modals
def test_connection_update_modal(clickOn, screenDiffChecker):
    clickOn(modal.connection_info_close)
    clickOn(btn.connection_update)
    time.sleep(2)
    assert screenDiffChecker(
        'interfaces/connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.interface_connection_modals
def test_connection_wifi_pass_modal(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.connection_choose_wifi)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.interface_connection_modals
def test_reset(clickOn, screenDiffChecker):
    clickOn(modal.wifi_pwd_close)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
