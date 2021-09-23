#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
32.84 seconds
'''


@pytest.mark.interface_quick_access
def test_charge_app(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'interfaces/charge_app.png'
    ) is None


@pytest.mark.interface_quick_access
def test_auto_tumbler_enable(click, type, screenDiffChecker):
    click(btn.charge_app_close)
    time.sleep(modals)
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.auto_mode)
    assert screenDiffChecker(
        'interfaces/control_auto_mode_enable.png'
    ) is None


@pytest.mark.interface_quick_access
def test_phrase_tumbler_enable(click, screenDiffChecker):
    click(btn.auto_mode)
    click(btn.phrase_mode)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/control_phrase_mode_enable.png'
    ) is None


@pytest.mark.interface_quick_access
def test_answerlog_tumbler_enable(click, screenDiffChecker):
    click(btn.phrase_mode)
    time.sleep(modals)
    click(btn.answers_log)
    assert screenDiffChecker(
        'interfaces/control_answers_log_enable.png'
    ) is None


@pytest.mark.interface_quick_access
def test_restart_modal(click, screenDiffChecker):
    click(btn.answers_log)
    click(btn.restart)
    assert screenDiffChecker(
        'interfaces/restart.png'
    ) is None


@pytest.mark.interface_quick_access
def test_hide(click, screenDiffChecker):
    click(modal.restart_no)
    click(btn.hide)
    assert screenDiffChecker(
        'interfaces/ubuntu_screen.png',
        (150, 40, 1280, 800)
    ) is None


@pytest.mark.interface_quick_access
def test_restore(click):
    click(btn.activities)
    click(btn.work_space)
    click(btn.work_space)
    click(btn.back)
    time.sleep(modals)
