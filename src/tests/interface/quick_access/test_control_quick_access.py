#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
32.84 seconds
'''


@pytest.mark.interface_quick_access
def test_charge_app(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'interfaces/charge_app.png'
    ) is None


@pytest.mark.interface_quick_access
def test_auto_tumbler_enable(clickOn, typeText, screenDiffChecker):
    clickOn(btn.charge_app_close)
    time.sleep(modals)
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.auto_mode)
    assert screenDiffChecker(
        'interfaces/control_auto_mode_enable.png'
    ) is None


@pytest.mark.interface_quick_access
def test_phrase_tumbler_enable(clickOn, screenDiffChecker):
    clickOn(btn.auto_mode)
    clickOn(btn.phrase_mode)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/control_phrase_mode_enable.png'
    ) is None


@pytest.mark.interface_quick_access
def test_answerlog_tumbler_enable(clickOn, screenDiffChecker):
    clickOn(btn.phrase_mode)
    time.sleep(modals)
    clickOn(btn.answers_log)
    assert screenDiffChecker(
        'interfaces/control_answers_log_enable.png'
    ) is None


@pytest.mark.interface_quick_access
def test_restart_modal(clickOn, screenDiffChecker):
    clickOn(btn.answers_log)
    clickOn(btn.restart)
    assert screenDiffChecker(
        'interfaces/restart.png'
    ) is None


@pytest.mark.interface_quick_access
def test_hide(clickOn, screenDiffChecker):
    clickOn(modal.restart_no)
    clickOn(btn.hide)
    assert screenDiffChecker(
        'interfaces/ubuntu_screen.png',
        (150, 40, 1280, 800)
    ) is None


@pytest.mark.interface_quick_access
def test_restore(clickOn, screenDiffChecker):
    clickOn(btn.activities)
    clickOn(btn.work_space)
    clickOn(btn.work_space)
    clickOn(btn.back)
    time.sleep(modals)
