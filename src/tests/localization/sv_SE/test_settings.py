#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal
'''
X seconds
'''


@pytest.mark.localization_sv_SE
def test_settings(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    assert screenDiffChecker(
        'localization/sv_SE/settings.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_system(clickOn, typeText, screenDiffChecker):
    clickOn(btn.system)
    assert screenDiffChecker(
        'localization/sv_SE/system.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_system_interaction(clickOn, screenDiffChecker):
    clickOn(btn.system_interaction)
    assert screenDiffChecker(
        'localization/sv_SE/system_interaction.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_system_menu_panel(clickOn, screenDiffChecker):
    clickOn(btn.system_menu_panel)
    assert screenDiffChecker(
        'localization/sv_SE/system_menu_panel.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_system_mic_array(clickOn, screenDiffChecker):
    clickOn(btn.system_mic_array)
    assert screenDiffChecker(
        'localization/sv_SE/system_mic_array.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_system_reset(clickOn, screenDiffChecker):
    clickOn(btn.system_reset)
    assert screenDiffChecker(
        'localization/sv_SE/system_reset.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_applications(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.apps)
    assert screenDiffChecker(
        'localization/sv_SE/applications.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.fr)
    assert screenDiffChecker(
        'localization/sv_SE/face_recognize.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_fr_facedb(clickOn, screenDiffChecker):
    clickOn(btn.fr_facedb)
    assert screenDiffChecker(
        'localization/sv_SE/face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_fr_adding_faces_modal(clickOn, screenDiffChecker):
    clickOn(btn.fr_facedb_select_folder)
    assert screenDiffChecker(
        'localization/sv_SE/adding_faces_modal.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_navigation(clickOn, screenDiffChecker):
    clickOn(modal.add_faces_close)
    clickOn(btn.back)
    clickOn(btn.nav)
    assert screenDiffChecker(
        'localization/sv_SE/navigation.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_save_parameters(clickOn, screenDiffChecker):
    clickOn(btn.useRadius)
    clickOn(btn.useRadius)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    assert screenDiffChecker(
        'localization/sv_SE/save_parameters.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_lingvo(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.lingvo)
    assert screenDiffChecker(
        'localization/sv_SE/lingvo.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_lingvo_sources(clickOn, screenDiffChecker):
    clickOn(btn.lingvo_sources)
    assert screenDiffChecker(
        'localization/sv_SE/lingvo_sources.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_language_settings(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.lang_settings)
    assert screenDiffChecker(
        'localization/sv_SE/language_settings.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_internet_services(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.internet)
    assert screenDiffChecker(
        'localization/sv_SE/internet_services.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_internet_services_sip(clickOn, screenDiffChecker):
    clickOn(btn.internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/sv_SE/internet_services_sip.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_internet_services_ya_disk(clickOn, screenDiffChecker):
    clickOn(btn.internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/sv_SE/internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_update(clickOn, screenDiffChecker):
    clickOn(btn.back)
    time.sleep(default)
    clickOn(btn.update)
    assert screenDiffChecker(
        'localization/sv_SE/update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_sv_SE
def test_reset(clickOn):
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
