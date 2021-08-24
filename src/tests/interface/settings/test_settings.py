#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.testConfig import default_timeout, modals_timeout
'''
17.87 seconds
'''


@pytest.mark.interface_settings
def test_settings_open(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('settings')
    assert screenDiffChecker(
        'interfaces/settings.png'
    ) is None


@pytest.mark.interface_settings
def test_system(clickOn, screenDiffChecker):
    clickOn('system')
    assert screenDiffChecker(
        'interfaces/system.png'
    ) is None


@pytest.mark.interface_settings
def test_applications(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('applications')
    assert screenDiffChecker(
        'interfaces/applications.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('face_recognize')
    assert screenDiffChecker(
        'interfaces/face_recognize.png'
    ) is None


@pytest.mark.interface_settings
def test_navigation(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('navigation')
    assert screenDiffChecker(
        'interfaces/navigation.png'
    ) is None


@pytest.mark.interface_settings
def test_lingvo(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('lingvo')
    assert screenDiffChecker(
        'interfaces/lingvo.png'
    ) is None


@pytest.mark.interface_settings
def test_language_settings(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('language_settings')
    assert screenDiffChecker(
        'interfaces/language_settings.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('internet_services')
    assert screenDiffChecker(
        'interfaces/internet_services.png'
    ) is None


@pytest.mark.interface_settings
def test_reset(clickOn):
    clickOn('back')
    time.sleep(default_timeout)
    clickOn('back')
    clickOn('back')
    time.sleep(modals_timeout)
