#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal, params
'''
32.73 seconds
'''


@pytest.mark.localization_it_IT
def test_settings(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    assert screenDiffChecker(
        'localization/it_IT/settings.png'
    ) is None


@pytest.mark.localization_it_IT
def test_system(clickOn, typeText, screenDiffChecker):
    clickOn(btn.system)
    assert screenDiffChecker(
        'localization/it_IT/system.png'
    ) is None


@pytest.mark.localization_it_IT
def test_system_interaction(clickOn, screenDiffChecker):
    clickOn(btn.system_interaction)
    assert screenDiffChecker(
        'localization/it_IT/system_interaction.png'
    ) is None


@pytest.mark.localization_it_IT
def test_system_menu_panel(clickOn, screenDiffChecker):
    clickOn(btn.system_menu_panel)
    assert screenDiffChecker(
        'localization/it_IT/system_menu_panel.png'
    ) is None


@pytest.mark.localization_it_IT
def test_system_mic_array(clickOn, screenDiffChecker):
    clickOn(btn.system_mic_array)
    assert screenDiffChecker(
        'localization/it_IT/system_mic_array.png'
    ) is None


@pytest.mark.localization_it_IT
def test_system_reset(clickOn, screenDiffChecker):
    clickOn(btn.system_reset)
    assert screenDiffChecker(
        'localization/it_IT/system_reset.png'
    ) is None


@pytest.mark.localization_it_IT
def test_applications(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.apps)
    assert screenDiffChecker(
        'localization/it_IT/applications.png'
    ) is None


@pytest.mark.localization_it_IT
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.fr)
    assert screenDiffChecker(
        'localization/it_IT/face_recognize.png'
    ) is None


@pytest.mark.localization_it_IT
def test_fr_facedb(clickOn, screenDiffChecker):
    clickOn(btn.fr_facedb)
    assert screenDiffChecker(
        'localization/it_IT/face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_it_IT
def test_fr_adding_faces_modal(clickOn, screenDiffChecker):
    clickOn(btn.fr_facedb_select_folder)
    assert screenDiffChecker(
        'localization/it_IT/adding_faces_modal.png'
    ) is None


@pytest.mark.localization_it_IT
def test_navigation(clickOn, screenDiffChecker):
    clickOn(modal.add_faces_close)
    clickOn(btn.back)
    clickOn(btn.nav)
    assert screenDiffChecker(
        'localization/it_IT/navigation.png'
    ) is None


@pytest.mark.localization_it_IT
def test_save_parameters(clickOn, screenDiffChecker):
    clickOn(params.useRadius)
    clickOn(params.useRadius)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    assert screenDiffChecker(
        'localization/it_IT/save_parameters.png'
    ) is None


@pytest.mark.localization_it_IT
def test_lingvo(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.lingvo)
    assert screenDiffChecker(
        'localization/it_IT/lingvo.png'
    ) is None


@pytest.mark.localization_it_IT
def test_lingvo_sources(clickOn, screenDiffChecker):
    clickOn(btn.lingvo_sources)
    assert screenDiffChecker(
        'localization/it_IT/lingvo_sources.png'
    ) is None


@pytest.mark.localization_it_IT
def test_language_settings(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.lang_settings)
    assert screenDiffChecker(
        'localization/it_IT/language_settings.png'
    ) is None


@pytest.mark.localization_it_IT
def test_internet_services(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.internet)
    assert screenDiffChecker(
        'localization/it_IT/internet_services.png'
    ) is None


@pytest.mark.localization_it_IT
def test_internet_services_sip(clickOn, screenDiffChecker):
    clickOn(btn.internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/it_IT/internet_services_sip.png'
    ) is None


@pytest.mark.localization_it_IT
def test_internet_services_ya_disk(clickOn, screenDiffChecker):
    clickOn(btn.internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/it_IT/internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_it_IT
def test_update(clickOn, screenDiffChecker):
    clickOn(btn.back)
    time.sleep(default)
    clickOn(btn.update)
    assert screenDiffChecker(
        'localization/it_IT/update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_it_IT
def test_reset(clickOn):
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
