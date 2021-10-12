#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, default, slowly
'''
29.22 seconds
'''


@pytest.mark.localization_es_ES
def test_settings(click, typeText, screenDiffChecker):
    click(btn.start.control)
    typeText(123456)
    click(modal.pwd.ok)
    click(btn.control.settings)
    assert screenDiffChecker(
        'localization/es_ES/settings.png'
    ) is None


@pytest.mark.localization_es_ES
def test_system(click, screenDiffChecker):
    click(btn.settings.system)
    assert screenDiffChecker(
        'localization/es_ES/set_system.png'
    ) is None


@pytest.mark.localization_es_ES
def test_system_hardware(click, screenDiffChecker):
    click(btn.system.hardware)
    assert screenDiffChecker(
        'localization/es_ES/set_system_hardware.png'
    ) is None


@pytest.mark.localization_es_ES
def test_system_led(click, screenDiffChecker):
    click(btn.system.led)
    assert screenDiffChecker(
        'localization/es_ES/set_system_led.png'
    ) is None


@pytest.mark.localization_es_ES
def test_system_dialog(click, screenDiffChecker):
    click(btn.system.dialog)
    assert screenDiffChecker(
        'localization/es_ES/set_system_dialog.png'
    ) is None


@pytest.mark.localization_es_ES
def test_system_interaction(click, screenDiffChecker):
    click(btn.system.interaction)
    assert screenDiffChecker(
        'localization/es_ES/set_system_interaction.png'
    ) is None


@pytest.mark.localization_es_ES
def test_system_menu_panel(click, screenDiffChecker):
    click(btn.system.menu_panel)
    assert screenDiffChecker(
        'localization/es_ES/set_system_menu_panel.png'
    ) is None


@pytest.mark.localization_es_ES
def test_system_mic_array(click, screenDiffChecker):
    click(btn.system.mic_array)
    assert screenDiffChecker(
        'localization/es_ES/set_system_mic_array.png'
    ) is None


@pytest.mark.localization_es_ES
def test_system_reset(click, screenDiffChecker):
    click(btn.system.reset)
    assert screenDiffChecker(
        'localization/es_ES/set_system_reset.png'
    ) is None


@pytest.mark.localization_es_ES
def test_applications(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.apps)
    assert screenDiffChecker(
        'localization/es_ES/set_applications.png'
    ) is None


@pytest.mark.localization_es_ES
def test_face_recognize(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.fr)
    assert screenDiffChecker(
        'localization/es_ES/set_face_recognize.png'
    ) is None


@pytest.mark.localization_es_ES
def test_fr_facedb(click, screenDiffChecker):
    click(btn.fr.facedb)
    assert screenDiffChecker(
        'localization/es_ES/set_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_es_ES
def test_fr_adding_faces_modal(click, screenDiffChecker):
    click(btn.fr.facedb_select_folder)
    assert screenDiffChecker(
        'localization/es_ES/set_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_es_ES
def test_navigation(click, screenDiffChecker):
    click(modal.add_face.close)
    click(btn.handler.back)
    click(btn.settings.nav)
    assert screenDiffChecker(
        'localization/es_ES/set_navigation.png'
    ) is None


@pytest.mark.localization_es_ES
def test_save_parameters_modal(click, screenDiffChecker):
    click(btn.nav.useRadius)
    click(btn.nav.useRadius)
    click(btn.handler.back)
    assert screenDiffChecker(
        'localization/es_ES/set_save_parameters_modal.png'
    ) is None


@pytest.mark.localization_es_ES
def test_save_parameters_popup(click, screenDiffChecker):
    click(modal.save.yes)
    assert screenDiffChecker(
        'localization/es_ES/set_save_parameters_popup.png'
    ) is None


@pytest.mark.localization_es_ES
def test_lingvo(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.settings.lingvo)
    assert screenDiffChecker(
        'localization/es_ES/set_lingvo.png'
    ) is None


@pytest.mark.localization_es_ES
def test_lingvo_sources(click, screenDiffChecker):
    click(btn.lingvo.sources)
    assert screenDiffChecker(
        'localization/es_ES/set_lingvo_sources.png'
    ) is None


@pytest.mark.localization_es_ES
def test_language_settings(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.lang)
    assert screenDiffChecker(
        'localization/es_ES/set_language_settings.png'
    ) is None


@pytest.mark.localization_es_ES
def test_internet_services(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.internet)
    assert screenDiffChecker(
        'localization/es_ES/set_internet_services.png'
    ) is None


@pytest.mark.localization_es_ES
def test_internet_services_sip(click, screenDiffChecker):
    click(btn.internet.sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/es_ES/set_internet_services_sip.png'
    ) is None


@pytest.mark.localization_es_ES
def test_internet_services_ya_disk(click, screenDiffChecker):
    click(btn.internet.ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/es_ES/set_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_es_ES
def test_update(click, screenDiffChecker):
    click(btn.handler.back)
    time.sleep(default)
    click(btn.settings.update)
    assert screenDiffChecker(
        'localization/es_ES/set_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_es_ES
def test_reset(click):
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.reset)
