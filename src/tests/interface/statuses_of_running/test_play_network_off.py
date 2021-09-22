#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly, running, restart, btn, modal
'''
92.24 seconds
'''


@pytest.mark.interface_statuses_of_running
def test_networkOff_modal(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(35)
    clickOn(btn.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/no_connection_modal.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn(modal.no_connection_yes)
    clickOn(modal.radius_yes)
    assert screenDiffChecker(
        'interfaces/run_state.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'interfaces/run_active.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'interfaces/run.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_restore(clickOn, openServiceMenu):
    time.sleep(running)
    openServiceMenu()
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
