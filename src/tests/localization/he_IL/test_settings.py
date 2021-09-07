#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal, params
'''
X seconds
'''


@pytest.mark.localization_he_IL
def test_settings(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.inv_settings)
    assert screenDiffChecker(
        'localization/he_IL/settings.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system(clickOn, typeText, screenDiffChecker):
    clickOn(btn.inv_system)
    assert screenDiffChecker(
        'localization/he_IL/system.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_interaction(clickOn, screenDiffChecker):
    clickOn(btn.inv_system_interaction)
    assert screenDiffChecker(
        'localization/he_IL/system_interaction.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_menu_panel(clickOn, screenDiffChecker):
    clickOn(btn.inv_system_menu_panel)
    assert screenDiffChecker(
        'localization/he_IL/system_menu_panel.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_mic_array(clickOn, screenDiffChecker):
    clickOn(btn.inv_system_mic_array)
    assert screenDiffChecker(
        'localization/he_IL/system_mic_array.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_reset(clickOn, screenDiffChecker):
    clickOn(btn.inv_system_reset)
    assert screenDiffChecker(
        'localization/he_IL/system_reset.png'
    ) is None


@pytest.mark.localization_he_IL
def test_applications(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(btn.inv_apps)
    assert screenDiffChecker(
        'localization/he_IL/applications.png'
    ) is None


@pytest.mark.localization_he_IL
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(btn.inv_fr)
    assert screenDiffChecker(
        'localization/he_IL/face_recognize.png'
    ) is None


@pytest.mark.localization_he_IL
def test_fr_facedb(clickOn, screenDiffChecker):
    clickOn(btn.inv_fr_facedb)
    assert screenDiffChecker(
        'localization/he_IL/face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_he_IL
def test_fr_adding_faces_modal(clickOn, screenDiffChecker):
    clickOn(btn.inv_fr_facedb_select_folder)
    assert screenDiffChecker(
        'localization/he_IL/adding_faces_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_navigation(clickOn, screenDiffChecker):
    clickOn(modal.inv_add_faces_close)
    clickOn(btn.inv_back)
    clickOn(btn.inv_nav)
    assert screenDiffChecker(
        'localization/he_IL/navigation.png'
    ) is None


@pytest.mark.localization_he_IL
def test_save_parameters(clickOn, screenDiffChecker):
    clickOn(params.inv_useRadius)
    clickOn(params.inv_useRadius)
    clickOn(btn.inv_back)
    clickOn(modal.inv_save_yes)
    assert screenDiffChecker(
        'localization/he_IL/save_parameters.png'
    ) is None


@pytest.mark.localization_he_IL
def test_lingvo(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.inv_lingvo)
    assert screenDiffChecker(
        'localization/he_IL/lingvo.png'
    ) is None


@pytest.mark.localization_he_IL
def test_lingvo_sources(clickOn, screenDiffChecker):
    clickOn(btn.inv_lingvo_sources)
    assert screenDiffChecker(
        'localization/he_IL/lingvo_sources.png'
    ) is None


@pytest.mark.localization_he_IL
def test_language_settings(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(btn.inv_lang_settings)
    assert screenDiffChecker(
        'localization/he_IL/language_settings.png'
    ) is None


@pytest.mark.localization_he_IL
def test_internet_services(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(btn.inv_internet)
    assert screenDiffChecker(
        'localization/he_IL/internet_services.png'
    ) is None


@pytest.mark.localization_he_IL
def test_internet_services_sip(clickOn, screenDiffChecker):
    clickOn(btn.inv_internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/internet_services_sip.png'
    ) is None


@pytest.mark.localization_he_IL
def test_internet_services_ya_disk(clickOn, screenDiffChecker):
    clickOn(btn.inv_internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_he_IL
def test_update(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    time.sleep(default)
    clickOn(btn.inv_update)
    assert screenDiffChecker(
        'localization/he_IL/update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_he_IL
def test_reset(clickOn):
    clickOn(btn.inv_back)
    clickOn(btn.inv_back)
    clickOn(btn.inv_back)
    time.sleep(modals)
