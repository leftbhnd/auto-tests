#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, slowly, running, restart
'''
58.51 seconds
'''


@pytest.mark.interface_statuses_of_running
def test_check_radius_modal(click, screenDiffChecker):
    click(btn.start.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/radius_modal.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_check_run_state(click, screenDiffChecker):
    click(modal.radius.yes)
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
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
