#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal
'''
31.53 seconds
'''


@pytest.mark.interface_settings
def test_system_hardware(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.system)
    clickOn(btn.system_hardware)
    assert screenDiffChecker(
        'interfaces/system_hardware.png'
    ) is None


@pytest.mark.interface_settings
def test_system_led(clickOn, screenDiffChecker):
    clickOn(btn.system_led)
    assert screenDiffChecker(
        'interfaces/system_led.png'
    ) is None


@pytest.mark.interface_settings
def test_system_dialog(clickOn, screenDiffChecker):
    clickOn(btn.system_dialog)
    assert screenDiffChecker(
        'interfaces/system_dialog.png'
    ) is None


@pytest.mark.interface_settings
def test_system_interaction(clickOn, screenDiffChecker):
    clickOn(btn.system_interaction)
    assert screenDiffChecker(
        'interfaces/system_interaction.png'
    ) is None


@pytest.mark.interface_settings
def test_system_menu_panel(clickOn, screenDiffChecker):
    clickOn(btn.system_menu_panel)
    assert screenDiffChecker(
        'interfaces/system_menu_panel.png'
    ) is None


@pytest.mark.interface_settings
def test_system_reset(clickOn, screenDiffChecker):
    clickOn(btn.system_reset)
    assert screenDiffChecker(
        'interfaces/system_reset.png'
    ) is None


@pytest.mark.interface_settings
def test_system_mic_array(clickOn, screenDiffChecker):
    clickOn(btn.system_mic_array)
    assert screenDiffChecker(
        'interfaces/system_mic_array.png'
    ) is None


@pytest.mark.interface_settings
def test_applications_apps(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.apps)
    clickOn(btn.apps_main)
    clickOn(btn.apps_applications)
    assert screenDiffChecker(
        'interfaces/applications_apps.png'
    ) is None


@pytest.mark.interface_settings
def test_applications_widgets(clickOn, screenDiffChecker):
    clickOn(btn.apps_applications)
    clickOn(btn.apps_widgets)
    assert screenDiffChecker(
        'interfaces/applications_widgets.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize_tracker(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.fr)
    clickOn(btn.fr_tacker)
    assert screenDiffChecker(
        'interfaces/face_recognize_tracker.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize_facedb(clickOn, screenDiffChecker):
    clickOn(btn.fr_facedb)
    assert screenDiffChecker(
        'interfaces/face_recognize_facedb.png'
    ) is None


@pytest.mark.interface_settings
def test_navigation_navigation(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.nav)
    clickOn(btn.nav_navigation)
    assert screenDiffChecker(
        'interfaces/navigation_navigation.png'
    ) is None


@pytest.mark.interface_settings
def test_lingvo_sources(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.lingvo)
    clickOn(btn.lingvo_sources)
    assert screenDiffChecker(
        'interfaces/lingvo_sources.png'
    ) is None


@pytest.mark.interface_settings
def test_language_settings_synthesis(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.lang_settings)
    clickOn(btn.lang_settings_synthesis)
    assert screenDiffChecker(
        'interfaces/language_settings_synthesis.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services_sip(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.internet)
    clickOn(btn.internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/internet_services_sip.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services_ya_disk(clickOn, screenDiffChecker):
    clickOn(btn.internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/internet_services_ya_disk.png'
    ) is None


@pytest.mark.interface_settings
def test_reset(clickOn):
    clickOn(btn.back)
    time.sleep(default)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
