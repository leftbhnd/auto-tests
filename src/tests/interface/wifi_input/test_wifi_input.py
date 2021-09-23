#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
21.72 seconds
'''


@pytest.mark.interface_wifi_input
def test_connection_open(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.interface_wifi_input
def test_hide_input(click, type, screenDiffChecker):
    time.sleep(modals)
    click(btn.connection_choose_wifi)
    click(modal.wifi_pwd_input)
    click(btn.choose_numbers)
    type('2281488')
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/wifi_hide_pass.png',
        (365, 162, 548, 200)
    ) is None


@pytest.mark.interface_wifi_input
def test_visiable_input(click, screenDiffChecker):
    click(modal.wifi_kb_pwd_eye)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/wifi_visiable_pass.png',
        (365, 162, 548, 200)
    ) is None


@pytest.mark.interface_wifi_input
def test_reset(click):
    click(modal.wifi_kb_pwd_close)
    click(btn.back)
    click(btn.back)
    time.sleep(modals)
