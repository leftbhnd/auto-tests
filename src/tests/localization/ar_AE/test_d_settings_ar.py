#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal, params
'''
33.10 seconds
'''


@pytest.mark.localization_ar_AE
def test_settings(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.change_lang)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.inv_settings)
    assert screenDiffChecker(
        'localization/ar_AE/settings.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system(clickOn, screenDiffChecker):
    clickOn(btn.inv_system)
    assert screenDiffChecker(
        'localization/ar_AE/set_system.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system_interaction(clickOn, screenDiffChecker):
    clickOn(btn.inv_system_interaction)
    assert screenDiffChecker(
        'localization/ar_AE/set_system_interaction.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system_menu_panel(clickOn, screenDiffChecker):
    clickOn(btn.inv_system_menu_panel)
    assert screenDiffChecker(
        'localization/ar_AE/set_system_menu_panel.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system_mic_array(clickOn, screenDiffChecker):
    clickOn(btn.inv_system_mic_array)
    assert screenDiffChecker(
        'localization/ar_AE/set_system_mic_array.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_system_reset(clickOn, screenDiffChecker):
    clickOn(btn.inv_system_reset)
    assert screenDiffChecker(
        'localization/ar_AE/set_system_reset.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_applications(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(btn.inv_apps)
    assert screenDiffChecker(
        'localization/ar_AE/set_applications.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(btn.inv_fr)
    assert screenDiffChecker(
        'localization/ar_AE/set_face_recognize.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_fr_facedb(clickOn, screenDiffChecker):
    clickOn(btn.inv_fr_facedb)
    assert screenDiffChecker(
        'localization/ar_AE/set_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_fr_adding_faces_modal(clickOn, screenDiffChecker):
    clickOn(btn.inv_fr_facedb_select_folder)
    assert screenDiffChecker(
        'localization/ar_AE/set_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_navigation(clickOn, screenDiffChecker):
    clickOn(modal.inv_add_faces_close)
    clickOn(btn.inv_back)
    clickOn(btn.inv_nav)
    assert screenDiffChecker(
        'localization/ar_AE/set_navigation.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_save_parameters(clickOn, screenDiffChecker):
    clickOn(params.inv_useRadius)
    clickOn(params.inv_useRadius)
    clickOn(btn.inv_back)
    clickOn(modal.inv_save_yes)
    assert screenDiffChecker(
        'localization/ar_AE/set_save_parameters.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_lingvo(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.inv_lingvo)
    assert screenDiffChecker(
        'localization/ar_AE/set_lingvo.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_lingvo_sources(clickOn, screenDiffChecker):
    clickOn(btn.inv_lingvo_sources)
    assert screenDiffChecker(
        'localization/ar_AE/set_lingvo_sources.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_language_settings(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(btn.inv_lang_settings)
    assert screenDiffChecker(
        'localization/ar_AE/set_language_settings.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_internet_services(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(btn.inv_internet)
    assert screenDiffChecker(
        'localization/ar_AE/set_internet_services.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_internet_services_sip(clickOn, screenDiffChecker):
    clickOn(btn.inv_internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/set_internet_services_sip.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_internet_services_ya_disk(clickOn, screenDiffChecker):
    clickOn(btn.inv_internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/set_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_update(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    time.sleep(default)
    clickOn(btn.inv_update)
    assert screenDiffChecker(
        'localization/ar_AE/set_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_ar_AE
def test_reset(clickOn):
    clickOn(btn.inv_back)
    clickOn(btn.inv_back)
    clickOn(btn.inv_back)
    time.sleep(modals)
