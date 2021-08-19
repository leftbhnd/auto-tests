#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.testConfig import slower_timeout, modals_timeout
'''
X seconds
'''


@pytest.mark.localization_ru_RU
def test_settings(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('1234567')
    clickOn('pass_modal_ok')
    clickOn('settings')
    assert screenDiffChecker(
        'localization/ru_RU/ru_settings.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system(clickOn, typeText, screenDiffChecker):
    clickOn('system')
    assert screenDiffChecker(
        'localization/ru_RU/ru_system.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system_interaction(clickOn, screenDiffChecker):
    clickOn('system_interaction')
    assert screenDiffChecker(
        'localization/ru_RU/ru_system_interaction.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system_menu_panel(clickOn, screenDiffChecker):
    clickOn('system_menu_panel')
    assert screenDiffChecker(
        'localization/ru_RU/ru_system_menu_panel.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system_mic_array(clickOn, screenDiffChecker):
    clickOn('system_mic_array')
    assert screenDiffChecker(
        'localization/ru_RU/ru_system_mic_array.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_system_reset(clickOn, screenDiffChecker):
    clickOn('system_reset')
    assert screenDiffChecker(
        'localization/ru_RU/ru_system_reset.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_applications(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('applications')
    assert screenDiffChecker(
        'localization/ru_RU/ru_applications.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('face_recognize')
    assert screenDiffChecker(
        'localization/ru_RU/ru_face_recognize.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_fr_facedb(clickOn, screenDiffChecker):
    clickOn('fr_facedb')
    assert screenDiffChecker(
        'localization/ru_RU/ru_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_fr_adding_faces_modal(clickOn, screenDiffChecker):
    clickOn('fasedb_select_folder')
    assert screenDiffChecker(
        'localization/ru_RU/ru_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_navigation(clickOn, screenDiffChecker):
    clickOn('adding_faces_modal_close')
    clickOn('back')
    clickOn('navigation')
    assert screenDiffChecker(
        'localization/ru_RU/ru_navigation.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_lingvo(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('lingvo')
    assert screenDiffChecker(
        'localization/ru_RU/ru_lingvo.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_lingvo_sources(clickOn, screenDiffChecker):
    clickOn('lingvo_sources')
    assert screenDiffChecker(
        'localization/ru_RU/ru_lingvo_sources.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_language_settings(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('language_settings')
    assert screenDiffChecker(
        'localization/ru_RU/ru_language_settings.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_internet_services(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('internet_services')
    assert screenDiffChecker(
        'localization/ru_RU/ru_internet_services.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_internet_services_sip(clickOn, screenDiffChecker):
    clickOn('internet_services_sip')
    time.sleep(slower_timeout)
    assert screenDiffChecker(
        'localization/ru_RU/ru_internet_services_sip.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_internet_services_ya_disk(clickOn, screenDiffChecker):
    clickOn('internet_services_ya_disk')
    time.sleep(slower_timeout)
    assert screenDiffChecker(
        'localization/ru_RU/ru_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_update(clickOn, screenDiffChecker):
    clickOn('back')
    time.sleep(default_timeout)
    clickOn('update')
    assert screenDiffChecker(
        'localization/ru_RU/ru_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_ru_RU
def test_reset(clickOn):
    clickOn('back')
    clickOn('back')
    time.sleep(modals_timeout)
