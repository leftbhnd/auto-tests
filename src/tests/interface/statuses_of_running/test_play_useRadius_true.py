#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.test_config import default_timeout, slower_timeout, running_timeout, restart_timeout
'''
58.51 seconds
'''


@pytest.mark.interface_statuses_of_running
def test_check_radius_modal(clickOn, screenDiffChecker):
    clickOn('play')
    time.sleep(slower_timeout)
    assert screenDiffChecker('radius_modal.png') is None


@pytest.mark.interface_statuses_of_running
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn('radius_modal_yes')
    assert screenDiffChecker('run_state.png') is None


@pytest.mark.interface_statuses_of_running
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker('run_active.png') is None


@pytest.mark.interface_statuses_of_running
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker('run.png') is None


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
