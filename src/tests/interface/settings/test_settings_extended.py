#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, default, slowly, modals
'''
31.53 seconds
'''


@pytest.mark.interface_settings
def test_system_hardware(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.system)
    click(btn.system.hardware)
    assert screenDiffChecker(
        'interfaces/system_hardware.png'
    ) is None


@pytest.mark.interface_settings
def test_system_led(click, screenDiffChecker):
    click(btn.system.led)
    assert screenDiffChecker(
        'interfaces/system_led.png'
    ) is None


@pytest.mark.interface_settings
def test_system_dialog(click, screenDiffChecker):
    click(btn.system.dialog)
    assert screenDiffChecker(
        'interfaces/system_dialog.png'
    ) is None


@pytest.mark.interface_settings
def test_system_interaction(click, screenDiffChecker):
    click(btn.system.interaction)
    assert screenDiffChecker(
        'interfaces/system_interaction.png'
    ) is None


@pytest.mark.interface_settings
def test_system_menu_panel(click, screenDiffChecker):
    click(btn.system.menu_panel)
    assert screenDiffChecker(
        'interfaces/system_menu_panel.png'
    ) is None


@pytest.mark.interface_settings
def test_system_reset(click, screenDiffChecker):
    click(btn.system.reset)
    assert screenDiffChecker(
        'interfaces/system_reset.png'
    ) is None


@pytest.mark.interface_settings
def test_system_mic_array(click, screenDiffChecker):
    click(btn.system.mic_array)
    assert screenDiffChecker(
        'interfaces/system_mic_array.png'
    ) is None


@pytest.mark.interface_settings
def test_applications_apps(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.apps)
    click(btn.apps.home)
    click(btn.apps.applications)
    assert screenDiffChecker(
        'interfaces/applications_apps.png'
    ) is None


@pytest.mark.interface_settings
def test_applications_widgets(click, screenDiffChecker):
    click(btn.apps.applications)
    click(btn.apps.widgets)
    assert screenDiffChecker(
        'interfaces/applications_widgets.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize_tracker(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.fr)
    click(btn.fr.tacker)
    assert screenDiffChecker(
        'interfaces/face_recognize_tracker.png'
    ) is None


@pytest.mark.interface_settings
def test_face_recognize_facedb(click, screenDiffChecker):
    click(btn.fr.facedb)
    assert screenDiffChecker(
        'interfaces/face_recognize_facedb.png'
    ) is None


@pytest.mark.interface_settings
def test_navigation_navigation(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.nav)
    click(btn.nav.navigation)
    assert screenDiffChecker(
        'interfaces/navigation_navigation.png'
    ) is None


@pytest.mark.interface_settings
def test_lingvo_sources(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.lingvo)
    click(btn.lingvo.sources)
    assert screenDiffChecker(
        'interfaces/lingvo_sources.png'
    ) is None


@pytest.mark.interface_settings
def test_language_settings_synthesis(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.lang)
    click(btn.lang.synthesis)
    assert screenDiffChecker(
        'interfaces/language_settings_synthesis.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services_sip(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.internet)
    click(btn.internet.sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/internet_services_sip.png'
    ) is None


@pytest.mark.interface_settings
def test_internet_services_ya_disk(click, screenDiffChecker):
    click(btn.internet.ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'interfaces/internet_services_ya_disk.png'
    ) is None


@pytest.mark.interface_settings
def test_reset(click):
    click(btn.handler.back)
    time.sleep(default)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(modals)
