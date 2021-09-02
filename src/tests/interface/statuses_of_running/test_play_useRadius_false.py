#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, modals, running, restart, btn, modal, params
'''
115.20 seconds
'''


@pytest.mark.interface_statuses_of_running
def test_disable_radius(node, clickOn, typeText):
    node.initNode()
    clickOn(btn.control)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.nav)
    clickOn(params.useRadius)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    assert node.getUseRadius() == False


@pytest.mark.interface_statuses_of_running
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn(btn.play)
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
def test_restore(openPasswordModal, clickOn, typeText, screenDiffChecker, node):
    time.sleep(running)
    openPasswordModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.nav)
    clickOn(params.useRadius)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    node.killNode()
    assert node.getUseRadius() == True
