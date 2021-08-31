#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, modals, btn, modal
'''
17.87 seconds
'''


@pytest.mark.interface_settings
def test_settings_open(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    assert screenDiffChecker(
        'interfaces/settings.png'
    ) is None


@pytest.mark.interface_settings
def test_system(clickOn, screenDiffChecker):
    clickOn(btn.system)
    assert screenDiffChecker(
        'interfaces/system.png'
    ) is None


@pytest.mark.interface_settings
def test_applications(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.apps)
    assert screenDiffChecker(
        'interfaces/applications.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.fr)
    assert screenDiffChecker(
        'interfaces/face_recognize.png'
    ) is None


@pytest.mark.interface_settings
def test_navigation(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.nav)
    assert screenDiffChecker(
        'interfaces/navigation.png'
    ) is None


@pytest.mark.interface_settings
def test_lingvo(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.lingvo)
    assert screenDiffChecker(
        'interfaces/lingvo.png'
    ) is None


@pytest.mark.interface_settings
def test_language_settings(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.lang_settings)
    assert screenDiffChecker(
        'interfaces/language_settings.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.internet)
    assert screenDiffChecker(
        'interfaces/internet_services.png'
    ) is None


@pytest.mark.interface_settings
def test_reset(clickOn):
    clickOn(btn.back)
    time.sleep(default)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
