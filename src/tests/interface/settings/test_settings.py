#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, modals, btn, modal
'''
17.87 seconds
'''


@pytest.mark.interface_settings
def test_settings_open(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.settings)
    assert screenDiffChecker(
        'interfaces/settings.png'
    ) is None


@pytest.mark.interface_settings
def test_system(click, screenDiffChecker):
    click(btn.system)
    assert screenDiffChecker(
        'interfaces/system.png'
    ) is None


@pytest.mark.interface_settings
def test_applications(click, screenDiffChecker):
    click(btn.back)
    click(btn.apps)
    assert screenDiffChecker(
        'interfaces/applications.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize(click, screenDiffChecker):
    click(btn.back)
    click(btn.fr)
    assert screenDiffChecker(
        'interfaces/face_recognize.png'
    ) is None


@pytest.mark.interface_settings
def test_navigation(click, screenDiffChecker):
    click(btn.back)
    click(btn.nav)
    assert screenDiffChecker(
        'interfaces/navigation.png'
    ) is None


@pytest.mark.interface_settings
def test_lingvo(click, screenDiffChecker):
    click(btn.back)
    click(btn.lingvo)
    assert screenDiffChecker(
        'interfaces/lingvo.png'
    ) is None


@pytest.mark.interface_settings
def test_language_settings(click, screenDiffChecker):
    click(btn.back)
    click(btn.lang_settings)
    assert screenDiffChecker(
        'interfaces/language_settings.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services(click, screenDiffChecker):
    click(btn.back)
    click(btn.internet)
    assert screenDiffChecker(
        'interfaces/internet_services.png'
    ) is None


@pytest.mark.interface_settings
def test_reset(click):
    click(btn.back)
    time.sleep(default)
    click(btn.back)
    click(btn.back)
    time.sleep(modals)
