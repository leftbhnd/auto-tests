#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, running, restart, btn, modal, params
'''
115.20 seconds
'''


@pytest.mark.interface_statuses_of_running
def test_disable_radius(node, click, type):
    click(btn.control)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.settings)
    click(btn.nav)
    click(params.useRadius)
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    assert node.getUseRadius() == False


@pytest.mark.interface_statuses_of_running
def test_check_run_state(click, screenDiffChecker):
    click(btn.play)
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
def test_restore(click, openServiceMenu, node):
    time.sleep(running)
    openServiceMenu()
    click(btn.settings)
    click(btn.nav)
    click(params.useRadius)
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    assert node.getUseRadius() == True
