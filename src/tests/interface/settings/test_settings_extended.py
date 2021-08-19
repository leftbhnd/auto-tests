#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.testConfig import default_timeout, slower_timeout, modals_timeout
'''
31.13 seconds
'''


@pytest.mark.interface_settings
def test_system_hardware(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('settings')
    clickOn('system')
    clickOn('system_hardware')
    assert screenDiffChecker(
        'interfaces/system_hardware.png'
    ) is None


@pytest.mark.interface_settings
def test_system_led(clickOn, screenDiffChecker):
    clickOn('system_led')
    assert screenDiffChecker(
        'interfaces/system_led.png'
    ) is None


@pytest.mark.interface_settings
def test_system_dialog(clickOn, screenDiffChecker):
    clickOn('system_dialog')
    assert screenDiffChecker(
        'interfaces/system_dialog.png'
    ) is None


@pytest.mark.interface_settings
def test_system_interaction(clickOn, screenDiffChecker):
    clickOn('system_interaction')
    assert screenDiffChecker(
        'interfaces/system_interaction.png'
    ) is None


@pytest.mark.interface_settings
def test_system_menu_panel(clickOn, screenDiffChecker):
    clickOn('system_menu_panel')
    assert screenDiffChecker(
        'interfaces/system_menu_panel.png'
    ) is None


@pytest.mark.interface_settings
def test_system_reset(clickOn, screenDiffChecker):
    clickOn('system_reset')
    assert screenDiffChecker(
        'interfaces/system_reset.png'
    ) is None


@pytest.mark.interface_settings
def test_system_mic_array(clickOn, screenDiffChecker):
    clickOn('system_mic_array')
    assert screenDiffChecker(
        'interfaces/system_mic_array.png'
    ) is None


@pytest.mark.interface_settings
def test_applications_apps(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('applications')
    clickOn('applications_main')
    clickOn('applications_apps')
    assert screenDiffChecker(
        'interfaces/applications_apps.png'
    ) is None


@pytest.mark.interface_settings
def test_applications_widgets(clickOn, screenDiffChecker):
    clickOn('applications_apps')
    clickOn('applications_widgets')
    assert screenDiffChecker(
        'interfaces/applications_widgets.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize_tracker(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('face_recognize')
    clickOn('fr_tacker')
    assert screenDiffChecker(
        'interfaces/face_recognize_tracker.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize_facedb(clickOn, screenDiffChecker):
    clickOn('fr_facedb')
    assert screenDiffChecker(
        'interfaces/face_recognize_facedb.png'
    ) is None


@pytest.mark.interface_settings
def test_navigation_navigation(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('navigation')
    clickOn('nav_navigation')
    assert screenDiffChecker(
        'interfaces/navigation_navigation.png'
    ) is None


@pytest.mark.interface_settings
def test_lingvo_sources(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('lingvo')
    clickOn('lingvo_sources')
    assert screenDiffChecker(
        'interfaces/lingvo_sources.png'
    ) is None


@pytest.mark.interface_settings
def test_language_settings_synthesis(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('language_settings')
    clickOn('language_settings_synthesis')
    assert screenDiffChecker(
        'interfaces/language_settings_synthesis.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services_sip(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('internet_services')
    clickOn('internet_services_sip')
    time.sleep(slower_timeout)
    assert screenDiffChecker(
        'interfaces/internet_services_sip.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services_ya_disk(clickOn, screenDiffChecker):
    clickOn('internet_services_ya_disk')
    time.sleep(slower_timeout)
    assert screenDiffChecker(
        'interfaces/internet_services_ya_disk.png'
    ) is None


@pytest.mark.interface_settings
def test_reset(clickOn):
    clickOn('back')
    time.sleep(default_timeout)
    clickOn('back')
    clickOn('back')
    time.sleep(modals_timeout)
