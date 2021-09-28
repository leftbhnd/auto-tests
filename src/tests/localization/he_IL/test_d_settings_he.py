#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, param, default, slowly
'''
32.89 seconds
'''


@pytest.mark.localization_he_IL
def test_settings(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_he)
    click(btn.control.settings_he)
    assert screenDiffChecker(
        'localization/he_IL/settings.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system(click, screenDiffChecker):
    click(btn.settings.system_he)
    assert screenDiffChecker(
        'localization/he_IL/set_system.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_hardware(click, screenDiffChecker):
    click(btn.system.hardware_he)
    assert screenDiffChecker(
        'localization/he_IL/set_system_hardware.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_led(click, screenDiffChecker):
    click(btn.system.led_he)
    assert screenDiffChecker(
        'localization/he_IL/set_system_led.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_dialog(click, screenDiffChecker):
    click(btn.system.dialog_he)
    assert screenDiffChecker(
        'localization/he_IL/set_system_dialog.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_interaction(click, screenDiffChecker):
    click(btn.system.interaction_he)
    assert screenDiffChecker(
        'localization/he_IL/set_system_interaction.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_menu_panel(click, screenDiffChecker):
    click(btn.system.menu_panel_he)
    assert screenDiffChecker(
        'localization/he_IL/set_system_menu_panel.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_mic_array(click, screenDiffChecker):
    click(btn.system.mic_array_he)
    assert screenDiffChecker(
        'localization/he_IL/set_system_mic_array.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_reset(click, screenDiffChecker):
    click(btn.system.reset_he)
    assert screenDiffChecker(
        'localization/he_IL/set_system_reset.png'
    ) is None


@pytest.mark.localization_he_IL
def test_applications(click, screenDiffChecker):
    click(btn.handler.back_he)
    click(btn.settings.apps_he)
    assert screenDiffChecker(
        'localization/he_IL/set_applications.png'
    ) is None


@pytest.mark.localization_he_IL
def test_face_recognize(click, screenDiffChecker):
    click(btn.handler.back_he)
    click(btn.settings.fr_he)
    assert screenDiffChecker(
        'localization/he_IL/set_face_recognize.png'
    ) is None


@pytest.mark.localization_he_IL
def test_fr_facedb(click, screenDiffChecker):
    click(btn.fr.facedb_he)
    assert screenDiffChecker(
        'localization/he_IL/set_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_he_IL
def test_fr_adding_faces_modal(click, screenDiffChecker):
    click(btn.fr.facedb_select_folder_he)
    assert screenDiffChecker(
        'localization/he_IL/set_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_navigation(click, screenDiffChecker):
    click(modal.add_face.close_he)
    click(btn.handler.back_he)
    click(btn.settings.nav_he)
    assert screenDiffChecker(
        'localization/he_IL/set_navigation.png'
    ) is None


@pytest.mark.localization_he_IL
def test_save_parameters(click, screenDiffChecker):
    click(param.driving.useRadius_he)
    click(param.driving.useRadius_he)
    click(btn.handler.back_he)
    click(modal.save.yes_he)
    assert screenDiffChecker(
        'localization/he_IL/set_save_parameters.png'
    ) is None


@pytest.mark.localization_he_IL
def test_lingvo(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.settings.lingvo_he)
    assert screenDiffChecker(
        'localization/he_IL/set_lingvo.png'
    ) is None


@pytest.mark.localization_he_IL
def test_lingvo_sources(click, screenDiffChecker):
    click(btn.lingvo.sources_he)
    assert screenDiffChecker(
        'localization/he_IL/set_lingvo_sources.png'
    ) is None


@pytest.mark.localization_he_IL
def test_language_settings(click, screenDiffChecker):
    click(btn.handler.back_he)
    click(btn.settings.lang_he)
    assert screenDiffChecker(
        'localization/he_IL/set_language_settings.png'
    ) is None


@pytest.mark.localization_he_IL
def test_internet_services(click, screenDiffChecker):
    click(btn.handler.back_he)
    click(btn.settings.internet_he)
    assert screenDiffChecker(
        'localization/he_IL/set_internet_services.png'
    ) is None


@pytest.mark.localization_he_IL
def test_internet_services_sip(click, screenDiffChecker):
    click(btn.internet.sip_he)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/set_internet_services_sip.png'
    ) is None


@pytest.mark.localization_he_IL
def test_internet_services_ya_disk(click, screenDiffChecker):
    click(btn.internet.ya_disk_he)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/set_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_he_IL
def test_update(click, screenDiffChecker):
    click(btn.handler.back_he)
    time.sleep(default)
    click(btn.settings.update_he)
    assert screenDiffChecker(
        'localization/he_IL/set_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_he_IL
def test_reset(click):
    click(btn.handler.back_he)
    click(btn.handler.back_he)
    click(btn.handler.back_he)
    click(btn.handler.reset)
