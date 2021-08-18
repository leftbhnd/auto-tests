#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.test_config import modals_timeout
'''
22.52 seconds
'''


@pytest.mark.interface
def test_connection(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('connection')
    time.sleep(modals_timeout)
    assert screenDiffChecker('connection.png', (0, 40, 920, 150)) is None


@pytest.mark.interface
def test_promo(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('promo')
    assert screenDiffChecker('promo.png') is None


@pytest.mark.interface
def test_testing(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('testing')
    assert screenDiffChecker('testing.png') is None


@pytest.mark.interface
def test_settings(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('settings')
    assert screenDiffChecker('settings.png') is None


@pytest.mark.interface
def test_browser(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('browser')
    time.sleep(modals_timeout)
    assert screenDiffChecker('browser.png', (0, 40, 1280, 75)) is None


@pytest.mark.interface
def test_identification(clickOn, screenDiffChecker):
    clickOn('browser_close')
    clickOn('identification')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker('identification.png') is None


@pytest.mark.interface
def test_restore(clickOn, screenDiffChecker):
    clickOn('ident_modal_close')
    clickOn('back')
    time.sleep(modals_timeout)
