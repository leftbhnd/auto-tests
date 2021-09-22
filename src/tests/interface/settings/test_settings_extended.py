#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal
'''
31.53 seconds
'''


@pytest.mark.interface_settings
def test_system_hardware(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.settings)
    click(btn.system)
    click(btn.system_hardware)
    assert screenDiffChecker(
        'interfaces/system_hardware.png'
    ) is None


@pytest.mark.interface_settings
def test_system_led(click, screenDiffChecker):
    click(btn.system_led)
    assert screenDiffChecker(
        'interfaces/system_led.png'
    ) is None


@pytest.mark.interface_settings
def test_system_dialog(click, screenDiffChecker):
    click(btn.system_dialog)
    assert screenDiffChecker(
        'interfaces/system_dialog.png'
    ) is None


@pytest.mark.interface_settings
def test_system_interaction(click, screenDiffChecker):
    click(btn.system_interaction)
    assert screenDiffChecker(
        'interfaces/system_interaction.png'
    ) is None


@pytest.mark.interface_settings
def test_system_menu_panel(click, screenDiffChecker):
    click(btn.system_menu_panel)
    assert screenDiffChecker(
        'interfaces/system_menu_panel.png'
    ) is None


@pytest.mark.interface_settings
def test_system_reset(click, screenDiffChecker):
    click(btn.system_reset)
    assert screenDiffChecker(
        'interfaces/system_reset.png'
    ) is None


@pytest.mark.interface_settings
def test_system_mic_array(click, screenDiffChecker):
    click(btn.system_mic_array)
    assert screenDiffChecker(
        'interfaces/system_mic_array.png'
    ) is None


@pytest.mark.interface_settings
def test_applications_apps(click, screenDiffChecker):
    click(btn.back)
    click(btn.apps)
    click(btn.apps_main)
    click(btn.apps_applications)
    assert screenDiffChecker(
        'interfaces/applications_apps.png'
    ) is None


@pytest.mark.interface_settings
def test_applications_widgets(click, screenDiffChecker):
    click(btn.apps_applications)
    click(btn.apps_widgets)
    assert screenDiffChecker(
        'interfaces/applications_widgets.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize_tracker(click, screenDiffChecker):
    click(btn.back)
    click(btn.fr)
    click(btn.fr_tacker)
    assert screenDiffChecker(
        'interfaces/face_recognize_tracker.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize_facedb(click, screenDiffChecker):
    click(btn.fr_facedb)
    assert screenDiffChecker(
        'interfaces/face_recognize_facedb.png'
    ) is None


@pytest.mark.interface_settings
def test_navigation_navigation(click, screenDiffChecker):
    click(btn.back)
    click(btn.nav)
    click(btn.nav_navigation)
    assert screenDiffChecker(
        'interfaces/navigation_navigation.png'
    ) is None


@pytest.mark.interface_settings
def test_lingvo_sources(click, screenDiffChecker):
    click(btn.back)
    click(btn.lingvo)
    click(btn.lingvo_sources)
    assert screenDiffChecker(
        'interfaces/lingvo_sources.png'
    ) is None


@pytest.mark.interface_settings
def test_language_settings_synthesis(click, screenDiffChecker):
    click(btn.back)
    click(btn.lang_settings)
    click(btn.lang_settings_synthesis)
    assert screenDiffChecker(
        'interfaces/language_settings_synthesis.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services_sip(click, screenDiffChecker):
    click(btn.back)
    click(btn.internet)
    click(btn.internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/internet_services_sip.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services_ya_disk(click, screenDiffChecker):
    click(btn.internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/internet_services_ya_disk.png'
    ) is None


@pytest.mark.interface_settings
def test_reset(click):
    click(btn.back)
    time.sleep(default)
    click(btn.back)
    click(btn.back)
    time.sleep(modals)
