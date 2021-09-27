#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, slowly, running, restart
'''
101.09 seconds
'''


@pytest.mark.interface_statuses_of_running
def test_networkOff_modal(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(35)
    click(btn.start.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/no_connection_modal.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_radius_modal(click, screenDiffChecker):
    click(modal.no_connection.yes)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/radius_modal.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_run_state(click, screenDiffChecker):
    click(modal.radius.yes)
    assert screenDiffChecker(
        'interfaces/run_state.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'interfaces/run_active.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'interfaces/run.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_restore(click, openServiceMenu):
    time.sleep(running)
    openServiceMenu()
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
