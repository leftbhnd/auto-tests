#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.test_config import default_timeout, modals_timeout, running_timeout, restart_timeout
'''
110 seconds
'''


@pytest.mark.interface
def test_disable_radius(node, clickOn, typeText):
    clickOn('control')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('settings')
    clickOn('navigation')
    clickOn('useRadius')
    clickOn('back')
    clickOn('save_modal_yes')
    time.sleep(modals_timeout)
    clickOn('back')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(restart_timeout)
    assert node.getUseRadius() == False


@pytest.mark.interface
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn('play')
    assert screenDiffChecker('run_state.png') is None


@pytest.mark.interface
def test_check_run_active(screenDiffChecker):
    time.sleep(default_timeout)
    assert screenDiffChecker('run_active.png') is None


@pytest.mark.interface
def test_check_run(screenDiffChecker):
    time.sleep(default_timeout)
    assert screenDiffChecker('run.png') is None


@pytest.mark.interface
def test_restore(openPasswordModal, clickOn, typeText, screenDiffChecker, node):
    time.sleep(running_timeout)
    openPasswordModal()
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('settings')
    clickOn('navigation')
    clickOn('useRadius')
    clickOn('back')
    clickOn('save_modal_yes')
    time.sleep(modals_timeout)
    clickOn('back')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(restart_timeout)
    assert node.getUseRadius() == True
