#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
62.52 seconds
'''


@pytest.mark.control_buttons
def test_connection(clickOn, typeText, customScreenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('connection')
    time.sleep(5)
    assert customScreenDiffChecker(
        {
            'image': 'connection.png', 'coordinates': (0, 40, 920, 150)
        }
    ) is None


@pytest.mark.control_buttons
def test_promo(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('promo')
    assert screenDiffChecker('promo.png') is None


@pytest.mark.control_buttons
def test_testing(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('testing')
    assert screenDiffChecker('testing.png') is None


@pytest.mark.control_buttons
def test_settings(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('settings')
    assert screenDiffChecker('settings.png') is None


@pytest.mark.control_buttons
def test_browser(clickOn, customScreenDiffChecker):
    clickOn('back')
    clickOn('browser')
    time.sleep(5)
    assert customScreenDiffChecker(
        {
            'image': 'browser.png', 'coordinates': (0, 40, 1280, 75)
        }
    ) is None


@pytest.mark.control_buttons
def test_identification(clickOn, screenDiffChecker):
    clickOn('browser_close')
    clickOn('identification')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker('identification.png') is None


@pytest.mark.control_buttons
def test_restore(clickOn, screenDiffChecker):
    clickOn('ident_modal_close')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert screenDiffChecker('start.png') is None
