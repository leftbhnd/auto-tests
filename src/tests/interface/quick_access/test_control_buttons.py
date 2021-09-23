#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
23.40 seconds
'''


@pytest.mark.interface_quick_access
def test_connection(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.interface_quick_access
def test_promo(click, screenDiffChecker):
    click(btn.back)
    click(btn.promo)
    assert screenDiffChecker(
        'interfaces/promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.interface_quick_access
def test_testing(click, screenDiffChecker):
    click(btn.back)
    click(btn.testing)
    assert screenDiffChecker(
        'interfaces/testing.png'
    ) is None


@pytest.mark.interface_quick_access
def test_settings(click, screenDiffChecker):
    click(btn.back)
    click(btn.settings)
    assert screenDiffChecker(
        'interfaces/settings.png'
    ) is None


@pytest.mark.interface_quick_access
def test_browser(click, screenDiffChecker):
    click(btn.back)
    click(btn.browser)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/browser.png',
        (0, 40, 1280, 75)
    ) is None


@pytest.mark.interface_quick_access
def test_identification(click, screenDiffChecker):
    click(btn.browser_close)
    click(btn.ident)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/identification.png'
    ) is None


@pytest.mark.interface_quick_access
def test_restore(click):
    click(modal.ident_close)
    click(btn.back)
    time.sleep(modals)
