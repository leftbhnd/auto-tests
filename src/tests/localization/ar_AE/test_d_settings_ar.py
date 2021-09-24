#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, param, default, slowly, modals
'''
33.10 seconds
'''


@pytest.mark.localization_ar_AE
def test_settings(click, type, screenDiffChecker):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.lang)
    click(btn.kb.numbers)
    type('123456')
    click(modal.pwd.ok_ae)
    click(btn.control.settings_ae)
    assert screenDiffChecker(
        'localization/ar_AE/settings.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system(click, screenDiffChecker):
    click(btn.settings.system_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_system.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system_interaction(click, screenDiffChecker):
    click(btn.system.interaction_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_system_interaction.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system_menu_panel(click, screenDiffChecker):
    click(btn.system.menu_panel_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_system_menu_panel.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system_mic_array(click, screenDiffChecker):
    click(btn.system.mic_array_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_system_mic_array.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system_reset(click, screenDiffChecker):
    click(btn.system.reset_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_system_reset.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_applications(click, screenDiffChecker):
    click(btn.handler.back_ae)
    click(btn.settings.apps_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_applications.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_face_recognize(click, screenDiffChecker):
    click(btn.handler.back_ae)
    click(btn.settings.fr_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_face_recognize.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_fr_facedb(click, screenDiffChecker):
    click(btn.fr.facedb_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_fr_adding_faces_modal(click, screenDiffChecker):
    click(btn.fr.facedb_select_folder_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_navigation(click, screenDiffChecker):
    click(modal.add_face.close_ae)
    click(btn.handler.back_ae)
    click(btn.settings.nav_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_navigation.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_save_parameters(click, screenDiffChecker):
    click(param.driving.useRadius_ae)
    click(param.driving.useRadius_ae)
    click(btn.handler.back_ae)
    click(modal.save.yes_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_save_parameters.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_lingvo(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.settings.lingvo_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_lingvo.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_lingvo_sources(click, screenDiffChecker):
    click(btn.lingvo.sources_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_lingvo_sources.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_language_settings(click, screenDiffChecker):
    click(btn.handler.back_ae)
    click(btn.settings.lang_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_language_settings.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_internet_services(click, screenDiffChecker):
    click(btn.handler.back_ae)
    click(btn.settings.internet_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_internet_services.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_internet_services_sip(click, screenDiffChecker):
    click(btn.internet.sip_ae)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/set_internet_services_sip.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_internet_services_ya_disk(click, screenDiffChecker):
    click(btn.internet.ya_disk_ae)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/set_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_update(click, screenDiffChecker):
    click(btn.handler.back_ae)
    time.sleep(default)
    click(btn.settings.update_ae)
    assert screenDiffChecker(
        'localization/ar_AE/set_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_ar_AE
def test_reset(click):
    click(btn.handler.back_ae)
    click(btn.handler.back_ae)
    click(btn.handler.back_ae)
    time.sleep(modals)
