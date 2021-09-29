#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, connection
'''
22.52 seconds
'''


@pytest.mark.interface_wifi_input
def test_connection_open(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.connection)
    time.sleep(connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.interface_wifi_input
def test_hide_input(click, typeText, screenDiffChecker):
    click(btn.connection.choose_wifi)
    click(modal.wifi_pwd.input)
    click(btn.kb.numbers)
    typeText('2281488')
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/wifi_hide_pass.png',
        (365, 162, 548, 200)
    ) is None


@pytest.mark.interface_wifi_input
def test_visiable_input(click, screenDiffChecker):
    click(modal.wifi_pwd.kb_eye)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/wifi_visiable_pass.png',
        (365, 162, 548, 200)
    ) is None


@pytest.mark.interface_wifi_input
def test_reset(click):
    click(modal.wifi_pwd.kb_close)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.reset)
