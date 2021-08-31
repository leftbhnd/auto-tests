#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
21.72 seconds
'''


@pytest.mark.interface_wifi_input
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


@pytest.mark.interface_wifi_input
def test_hide_input(clickOn, typeText, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.connection_choose_wifi)
    clickOn(modal.wifi_pwd_input)
    clickOn(btn.choose_numbers)
    typeText('2281488')
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/wifi_hide_pass.png',
        (365, 162, 548, 200)
    ) is None


@pytest.mark.interface_wifi_input
def test_visiable_input(clickOn, screenDiffChecker):
    clickOn(modal.wifi_kb_pwd_eye)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/wifi_visiable_pass.png',
        (365, 162, 548, 200)
    ) is None


@pytest.mark.interface_wifi_input
def test_reset(clickOn, screenDiffChecker):
    clickOn(modal.wifi_kb_pwd_close)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
