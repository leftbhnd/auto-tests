#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.testConfig import default_timeout, slower_timeout, running_timeout, restart_timeout
'''
92.24 seconds
'''


@pytest.mark.interface_statuses_of_running
def test_networkOff_modal(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(30)
    clickOn('play')
    time.sleep(slower_timeout)
    assert screenDiffChecker(
        'interfaces/no_connection_modal.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn('no_connection_modal_yes')
    clickOn('radius_modal_yes')
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
def test_restore(openPasswordModal, clickOn, typeText, screenDiffChecker):
    time.sleep(running_timeout)
    openPasswordModal()
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(restart_timeout)
