#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time


'''
X seconds
'''


@pytest.mark.settings
def test_settings_open(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('settings')
    assert screenDiffChecker('settings.png') is None


@pytest.mark.settings
def test_system(clickOn, screenDiffChecker):
    clickOn('system')
    assert screenDiffChecker('system.png') is None


@pytest.mark.settings
def test_applications(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('applications')
    assert screenDiffChecker('applications.png') is None


@pytest.mark.settings
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('face_recognize')
    assert screenDiffChecker('face_recognize.png') is None


@pytest.mark.settings
def test_navigation(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('navigation')
    assert screenDiffChecker('navigation.png') is None


@pytest.mark.settings
def test_lingvo(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('lingvo')
    assert screenDiffChecker('lingvo.png') is None


@pytest.mark.settings
def test_language_settings(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('language_settings')
    assert screenDiffChecker('language_settings.png') is None


@pytest.mark.settings
def test_internet_services(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('internet_services')
    assert screenDiffChecker('internet_services.png') is None


@pytest.mark.settings
def test_update(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('update')
    assert screenDiffChecker('update.png') is None


@pytest.mark.settings
def test_reset(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert screenDiffChecker('start.png') is None
