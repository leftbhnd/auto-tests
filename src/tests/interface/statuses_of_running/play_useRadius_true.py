#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time


@pytest.mark.useRadiusTrue
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn('play')
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
    assert screenDiffChecker('start.png') is None
