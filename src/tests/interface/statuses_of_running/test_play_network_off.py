#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly, running, restart, btn, modal
'''
92.24 seconds
'''


@pytest.mark.interface_statuses_of_running
def test_networkOff_modal(click, type, screenDiffChecker):
    click(btn.control)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(35)
    click(btn.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/no_connection_modal.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_check_run_state(click, screenDiffChecker):
    click(modal.no_connection_yes)
    click(modal.radius_yes)
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
def test_restore(click, openServiceMenu):
    time.sleep(running)
    openServiceMenu()
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
