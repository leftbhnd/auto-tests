#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
32.83 seconds
'''


@pytest.mark.control_qa
def test_charge_app(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('send_to_charge')
    time.sleep(2)
    assert screenDiffChecker('charge_app.png') is None


@pytest.mark.control_qa
def test_auto_tumbler_disable(clickOn, typeText, screenDiffChecker):
    clickOn('send_to_charge_close')
    time.sleep(4)
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    assert screenDiffChecker('control.png') is None


@pytest.mark.control_qa
def test_auto_tumbler_enable(clickOn, screenDiffChecker):
    clickOn('auto_mode')
    assert screenDiffChecker('control_auto_mode_enable.png') is None


@pytest.mark.control_qa
def test_phrase_tumbler_enable(clickOn, screenDiffChecker):
    clickOn('auto_mode')
    clickOn('phrase_mode')
    time.sleep(4)
    assert screenDiffChecker('control_phrase_mode_enable.png') is None


@pytest.mark.control_qa
def test_answerlog_tumbler_enable(clickOn, screenDiffChecker):
    clickOn('phrase_mode')
    time.sleep(4)
    clickOn('answers_log')
    assert screenDiffChecker('control_answers_log_enable.png') is None


@pytest.mark.control_qa
def test_restart_modal(clickOn, screenDiffChecker):
    clickOn('answers_log')
    clickOn('restart')
    assert screenDiffChecker('restart.png') is None


@pytest.mark.control_qa
def test_hide(clickOn, customScreenDiffChecker):
    clickOn('restart_modal_no')
    clickOn('hide')
    assert customScreenDiffChecker(
        {
            'image': 'ubuntu_screen.png', 'coordinates': (150, 40, 1280, 800)
        }
    ) is None


@pytest.mark.control_qa
def test_restore(clickOn, screenDiffChecker):
    clickOn('activities')
    time.sleep(1)
    clickOn('work_space')
    time.sleep(1)
    clickOn('work_space')
    time.sleep(1)
    clickOn('back')
