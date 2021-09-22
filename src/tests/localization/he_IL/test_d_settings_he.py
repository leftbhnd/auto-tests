#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal, params
'''
32.89 seconds
'''


@pytest.mark.localization_he_IL
def test_settings(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.inv_pwd_ok)
    click(btn.inv_settings)
    assert screenDiffChecker(
        'localization/he_IL/settings.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system(click, screenDiffChecker):
    click(btn.inv_system)
    assert screenDiffChecker(
        'localization/he_IL/set_system.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_interaction(click, screenDiffChecker):
    click(btn.inv_system_interaction)
    assert screenDiffChecker(
        'localization/he_IL/set_system_interaction.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_menu_panel(click, screenDiffChecker):
    click(btn.inv_system_menu_panel)
    assert screenDiffChecker(
        'localization/he_IL/set_system_menu_panel.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_mic_array(click, screenDiffChecker):
    click(btn.inv_system_mic_array)
    assert screenDiffChecker(
        'localization/he_IL/set_system_mic_array.png'
    ) is None


@pytest.mark.localization_he_IL
def test_system_reset(click, screenDiffChecker):
    click(btn.inv_system_reset)
    assert screenDiffChecker(
        'localization/he_IL/set_system_reset.png'
    ) is None


@pytest.mark.localization_he_IL
def test_applications(click, screenDiffChecker):
    click(btn.inv_back)
    click(btn.inv_apps)
    assert screenDiffChecker(
        'localization/he_IL/set_applications.png'
    ) is None


@pytest.mark.localization_he_IL
def test_face_recognize(click, screenDiffChecker):
    click(btn.inv_back)
    click(btn.inv_fr)
    assert screenDiffChecker(
        'localization/he_IL/set_face_recognize.png'
    ) is None


@pytest.mark.localization_he_IL
def test_fr_facedb(click, screenDiffChecker):
    click(btn.inv_fr_facedb)
    assert screenDiffChecker(
        'localization/he_IL/set_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_he_IL
def test_fr_adding_faces_modal(click, screenDiffChecker):
    click(btn.inv_fr_facedb_select_folder)
    assert screenDiffChecker(
        'localization/he_IL/set_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_navigation(click, screenDiffChecker):
    click(modal.inv_add_faces_close)
    click(btn.inv_back)
    click(btn.inv_nav)
    assert screenDiffChecker(
        'localization/he_IL/set_navigation.png'
    ) is None


@pytest.mark.localization_he_IL
def test_save_parameters(click, screenDiffChecker):
    click(params.inv_useRadius)
    click(params.inv_useRadius)
    click(btn.inv_back)
    click(modal.inv_save_yes)
    assert screenDiffChecker(
        'localization/he_IL/set_save_parameters.png'
    ) is None


@pytest.mark.localization_he_IL
def test_lingvo(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.inv_lingvo)
    assert screenDiffChecker(
        'localization/he_IL/set_lingvo.png'
    ) is None


@pytest.mark.localization_he_IL
def test_lingvo_sources(click, screenDiffChecker):
    click(btn.inv_lingvo_sources)
    assert screenDiffChecker(
        'localization/he_IL/set_lingvo_sources.png'
    ) is None


@pytest.mark.localization_he_IL
def test_language_settings(click, screenDiffChecker):
    click(btn.inv_back)
    click(btn.inv_lang_settings)
    assert screenDiffChecker(
        'localization/he_IL/set_language_settings.png'
    ) is None


@pytest.mark.localization_he_IL
def test_internet_services(click, screenDiffChecker):
    click(btn.inv_back)
    click(btn.inv_internet)
    assert screenDiffChecker(
        'localization/he_IL/set_internet_services.png'
    ) is None


@pytest.mark.localization_he_IL
def test_internet_services_sip(click, screenDiffChecker):
    click(btn.inv_internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/set_internet_services_sip.png'
    ) is None


@pytest.mark.localization_he_IL
def test_internet_services_ya_disk(click, screenDiffChecker):
    click(btn.inv_internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/set_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_he_IL
def test_update(click, screenDiffChecker):
    click(btn.inv_back)
    time.sleep(default)
    click(btn.inv_update)
    assert screenDiffChecker(
        'localization/he_IL/set_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_he_IL
def test_reset(click):
    click(btn.inv_back)
    click(btn.inv_back)
    click(btn.inv_back)
    time.sleep(modals)
