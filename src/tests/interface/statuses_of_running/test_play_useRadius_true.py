#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
59 seconds
'''
@pytest.mark.useRadiusTrue
def test_check_radius_modal(clickOn, screenDiffChecker):
    clickOn('play')
    time.sleep(5)
    assert screenDiffChecker('radius_modal.png') is None


@pytest.mark.useRadiusTrue
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn('radius_modal_yes')
    assert screenDiffChecker('run_state.png') is None


@pytest.mark.useRadiusTrue
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker('run_active.png') is None


@pytest.mark.useRadiusTrue
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker('run.png') is None


@pytest.mark.useRadiusTrue
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
