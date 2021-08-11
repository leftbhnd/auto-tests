#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time


@pytest.mark.useRadiusTrue
def test_check_radius_modal(clickOn, screenDiffChecker):
    clickOn('play')
    assert screenDiffChecker('radius_modal.png') is None

@pytest.mark.useRadiusTrue
def test_check_run_active(clickOn, screenDiffChecker):
    clickOn('radius_modal_yes')
    assert screenDiffChecker('run_state.png') is None

@pytest.mark.useRadiusTrue
def test_check_run_active(screenDiffChecker):
    assert screenDiffChecker('run_active.png') is None


@pytest.mark.useRadiusTrue
def test_check_run(screenDiffChecker):
    assert screenDiffChecker('run.png') is None


@pytest.mark.useRadiusTrue
def test_open_menu(openPasswordModal, clickOn, typeText, screenDiffChecker):
    openPasswordModal()
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(10)
    assert screenDiffChecker('start.png') is None
