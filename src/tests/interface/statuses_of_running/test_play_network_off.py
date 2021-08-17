#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
97.35 seconds
'''
@pytest.mark.networkOff
def test_networkOff_modal(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(35)
    clickOn('play')
    time.sleep(5)
    assert screenDiffChecker('no_connection_modal.png') is None


@pytest.mark.networkOff
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn('no_connection_modal_yes')
    clickOn('radius_modal_yes')
    assert screenDiffChecker('run_state.png') is None


@pytest.mark.networkOff
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker('run_active.png') is None


@pytest.mark.networkOff
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker('run.png') is None


@pytest.mark.networkOff
def test_restore(openPasswordModal, clickOn, typeText, screenDiffChecker):
    time.sleep(6)
    openPasswordModal()
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert screenDiffChecker('start.png') is None
