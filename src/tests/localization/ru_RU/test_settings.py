#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal
'''
34.47 seconds
'''


@pytest.mark.localization_ru_RU
def test_settings(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    assert screenDiffChecker(
        'localization/ru_RU/settings.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system(clickOn, typeText, screenDiffChecker):
    clickOn(btn.system)
    assert screenDiffChecker(
        'localization/ru_RU/system.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system_interaction(clickOn, screenDiffChecker):
    clickOn(btn.system_interaction)
    assert screenDiffChecker(
        'localization/ru_RU/system_interaction.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system_menu_panel(clickOn, screenDiffChecker):
    clickOn(btn.system_menu_panel)
    assert screenDiffChecker(
        'localization/ru_RU/system_menu_panel.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system_mic_array(clickOn, screenDiffChecker):
    clickOn(btn.system_mic_array)
    assert screenDiffChecker(
        'localization/ru_RU/system_mic_array.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system_reset(clickOn, screenDiffChecker):
    clickOn(btn.system_reset)
    assert screenDiffChecker(
        'localization/ru_RU/system_reset.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_applications(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.apps)
    assert screenDiffChecker(
        'localization/ru_RU/applications.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.fr)
    assert screenDiffChecker(
        'localization/ru_RU/face_recognize.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_fr_facedb(clickOn, screenDiffChecker):
    clickOn(btn.fr_facedb)
    assert screenDiffChecker(
        'localization/ru_RU/face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_fr_adding_faces_modal(clickOn, screenDiffChecker):
    clickOn(btn.fr_facedb_select_folder)
    assert screenDiffChecker(
        'localization/ru_RU/adding_faces_modal.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_navigation(clickOn, screenDiffChecker):
    clickOn(modal.add_faces_close)
    clickOn(btn.back)
    clickOn(btn.nav)
    assert screenDiffChecker(
        'localization/ru_RU/navigation.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_save_parameters(clickOn, screenDiffChecker):
    clickOn(btn.useRadius)
    clickOn(btn.useRadius)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    assert screenDiffChecker(
        'localization/ru_RU/save_parameters.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_lingvo(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.lingvo)
    assert screenDiffChecker(
        'localization/ru_RU/lingvo.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_lingvo_sources(clickOn, screenDiffChecker):
    clickOn(btn.lingvo_sources)
    assert screenDiffChecker(
        'localization/ru_RU/lingvo_sources.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_language_settings(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.lang_settings)
    assert screenDiffChecker(
        'localization/ru_RU/language_settings.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_internet_services(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.internet)
    assert screenDiffChecker(
        'localization/ru_RU/internet_services.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_internet_services_sip(clickOn, screenDiffChecker):
    clickOn(btn.internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ru_RU/internet_services_sip.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_internet_services_ya_disk(clickOn, screenDiffChecker):
    clickOn(btn.internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ru_RU/internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_update(clickOn, screenDiffChecker):
    clickOn(btn.back)
    time.sleep(default)
    clickOn(btn.update)
    assert screenDiffChecker(
        'localization/ru_RU/update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_ru_RU
def test_reset(clickOn):
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
