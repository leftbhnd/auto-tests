#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
110 seconds
'''


@pytest.mark.useRadiusFalse
def test_disable_radius(node, clickOn, typeText):
    clickOn('control')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('settings')
    clickOn('navigation')
    clickOn('useRadius')
    clickOn('back')
    clickOn('save_modal_yes')
    time.sleep(3)
    clickOn('back')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert node.getUseRadius() == False


@pytest.mark.useRadiusFalse
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn('play')
    assert screenDiffChecker('run_state.png') is None


@pytest.mark.useRadiusFalse
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker('run_active.png') is None


@pytest.mark.useRadiusFalse
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker('run.png') is None


@pytest.mark.useRadiusFalse
def test_restore(openPasswordModal, clickOn, typeText, screenDiffChecker, node):
    time.sleep(5)
    openPasswordModal()
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('settings')
    clickOn('navigation')
    clickOn('useRadius')
    clickOn('back')
    clickOn('save_modal_yes')
    time.sleep(3)
    clickOn('back')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert node.getUseRadius() == True
