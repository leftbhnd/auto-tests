#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, default, modals
'''
17.87 seconds
'''


@pytest.mark.interface_settings
def test_settings_open(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.settings)
    assert screenDiffChecker(
        'interfaces/settings.png'
    ) is None


@pytest.mark.interface_settings
def test_system(click, screenDiffChecker):
    click(btn.settings.system)
    assert screenDiffChecker(
        'interfaces/system.png'
    ) is None


@pytest.mark.interface_settings
def test_applications(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.setting.apps)
    assert screenDiffChecker(
        'interfaces/applications.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.fr)
    assert screenDiffChecker(
        'interfaces/face_recognize.png'
    ) is None


@pytest.mark.interface_settings
def test_navigation(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.nav)
    assert screenDiffChecker(
        'interfaces/navigation.png'
    ) is None


@pytest.mark.interface_settings
def test_lingvo(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.lingvo)
    assert screenDiffChecker(
        'interfaces/lingvo.png'
    ) is None


@pytest.mark.interface_settings
def test_language_settings(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.lang)
    assert screenDiffChecker(
        'interfaces/language_settings.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.internet)
    assert screenDiffChecker(
        'interfaces/internet_services.png'
    ) is None


@pytest.mark.interface_settings
def test_reset(click):
    click(btn.handler.back)
    time.sleep(default)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(modals)
