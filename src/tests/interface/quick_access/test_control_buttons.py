#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
23.40 seconds
'''


@pytest.mark.interface_quick_access
def test_connection(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.interface_quick_access
def test_promo(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.promo)
    assert screenDiffChecker(
        'interfaces/promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.interface_quick_access
def test_testing(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.testing)
    assert screenDiffChecker(
        'interfaces/testing.png'
    ) is None


@pytest.mark.interface_quick_access
def test_settings(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.settings)
    assert screenDiffChecker(
        'interfaces/settings.png'
    ) is None


@pytest.mark.interface_quick_access
def test_browser(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.browser)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/browser.png',
        (0, 40, 1280, 75)
    ) is None


@pytest.mark.interface_quick_access
def test_identification(clickOn, screenDiffChecker):
    clickOn(btn.browser_close)
    clickOn(btn.ident)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/identification.png'
    ) is None


@pytest.mark.interface_quick_access
def test_restore(clickOn):
    clickOn(modal.ident_close)
    clickOn(btn.back)
    time.sleep(modals)
