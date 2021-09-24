#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
26.21 seconds
'''


@pytest.mark.interface_connection_modals
def test_connection_open(click, type, screenDiffChecker):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    type('123456')
    click(modal.pwd.ok)
    click(btn.control.connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.interface_connection_modals
def test_connection_info_modal(click, screenDiffChecker):
    click(btn.connection_info)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.interface_connection_modals
def test_connection_update_modal(click, screenDiffChecker):
    click(modal.connection_info.close)
    click(btn.connection.update)
    time.sleep(2)
    assert screenDiffChecker(
        'interfaces/connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.interface_connection_modals
def test_connection_wifi_pass_modal(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.connection.choose_wifi)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.interface_connection_modals
def test_reset(click):
    click(modal.wifi_pwd.close)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(modals)
