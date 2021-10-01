#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal
'''
16.58 seconds
'''


@pytest.mark.interface_quick_access
def test_charge_app(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'interfaces/charge_app.png'
    ) is None


@pytest.mark.interface_quick_access
def test_auto_tumbler_enable(click, typeText, screenDiffChecker):
    click(btn.control.charge_app_close)
    click(btn.handler.reset)
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.auto_mode)
    assert screenDiffChecker(
        'interfaces/control_auto_mode_enable.png',
        (780, 400, 450, 380)
    ) is None


@pytest.mark.interface_quick_access
def test_phrase_tumbler_enable(click, screenDiffChecker):
    click(btn.control.auto_mode)
    click(btn.control.phrase_mode)
    assert screenDiffChecker(
        'interfaces/control_phrase_mode_enable.png'
    ) is None


@pytest.mark.interface_quick_access
def test_answerlog_tumbler_enable(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.control.phrase_mode)
    click(btn.handler.reset)
    click(btn.control.answers_log)
    assert screenDiffChecker(
        'interfaces/control_answers_log_enable.png',
        (780, 400, 450, 380)
    ) is None


@pytest.mark.interface_quick_access
def test_restart_modal(click, screenDiffChecker):
    click(btn.control.answers_log)
    click(btn.control.restart)
    assert screenDiffChecker(
        'interfaces/restart.png',
        (350, 305, 580, 190)
    ) is None


@pytest.mark.interface_quick_access
def test_hide(click, screenDiffChecker):
    click(modal.restart.no)
    click(btn.control.hide)
    assert screenDiffChecker(
        'interfaces/ubuntu_screen.png',
        (150, 40, 1280, 800)
    ) is None


@pytest.mark.interface_quick_access
def test_restore(click):
    click(btn.ubuntu.activities)
    click(btn.ubuntu.work_space)
    click(btn.ubuntu.work_space)
    click(btn.handler.back)
    click(btn.handler.reset)
