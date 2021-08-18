#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.test_config import modals_timeout
'''
32.84 seconds
'''


@pytest.mark.interface
def test_charge_app(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('send_to_charge')
    time.sleep(2)
    assert screenDiffChecker('charge_app.png') is None


@pytest.mark.interface
def test_auto_tumbler_disable(clickOn, typeText, screenDiffChecker):
    clickOn('send_to_charge_close')
    time.sleep(modals_timeout)
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    assert screenDiffChecker('control.png') is None


@pytest.mark.interface
def test_auto_tumbler_enable(clickOn, screenDiffChecker):
    clickOn('auto_mode')
    assert screenDiffChecker('control_auto_mode_enable.png') is None


@pytest.mark.interface
def test_phrase_tumbler_enable(clickOn, screenDiffChecker):
    clickOn('auto_mode')
    clickOn('phrase_mode')
    time.sleep(modals_timeout)
    assert screenDiffChecker('control_phrase_mode_enable.png') is None


@pytest.mark.interface
def test_answerlog_tumbler_enable(clickOn, screenDiffChecker):
    clickOn('phrase_mode')
    time.sleep(modals_timeout)
    clickOn('answers_log')
    assert screenDiffChecker('control_answers_log_enable.png') is None


@pytest.mark.interface
def test_restart_modal(clickOn, screenDiffChecker):
    clickOn('answers_log')
    clickOn('restart')
    assert screenDiffChecker('restart.png') is None


@pytest.mark.interface
def test_hide(clickOn, screenDiffChecker):
    clickOn('restart_modal_no')
    clickOn('hide')
    assert screenDiffChecker('ubuntu_screen.png', (150, 40, 1280, 800)) is None


@pytest.mark.interface
def test_restore(clickOn, screenDiffChecker):
    clickOn('activities')
    clickOn('work_space')
    clickOn('work_space')
    clickOn('back')
    time.sleep(modals_timeout)
