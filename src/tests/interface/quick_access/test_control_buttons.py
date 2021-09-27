#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
23.40 seconds
'''


@pytest.mark.interface_quick_access
def test_connection(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.interface_quick_access
def test_promo(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.control.promo)
    assert screenDiffChecker(
        'interfaces/promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.interface_quick_access
def test_testing(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.control.testing)
    assert screenDiffChecker(
        'interfaces/testing.png'
    ) is None


@pytest.mark.interface_quick_access
def test_settings(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.control.settings)
    assert screenDiffChecker(
        'interfaces/settings.png'
    ) is None


@pytest.mark.interface_quick_access
def test_browser(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.control.browser)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/browser.png',
        (0, 40, 1280, 75)
    ) is None


@pytest.mark.interface_quick_access
def test_identification(click, screenDiffChecker):
    click(btn.control.browser_close)
    click(btn.control.ident)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/identification.png'
    ) is None


@pytest.mark.interface_quick_access
def test_restore(click):
    click(modal.ident.close)
    click(btn.handler.back)
    time.sleep(modals)
