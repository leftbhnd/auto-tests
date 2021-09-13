#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal, params
'''
32.60 seconds
'''


@pytest.mark.localization_zh_CN
def test_settings(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    assert screenDiffChecker(
        'localization/zh_CN/settings.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_system(clickOn, typeText, screenDiffChecker):
    clickOn(btn.system)
    assert screenDiffChecker(
        'localization/zh_CN/set_system.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_system_interaction(clickOn, screenDiffChecker):
    clickOn(btn.system_interaction)
    assert screenDiffChecker(
        'localization/zh_CN/set_system_interaction.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_system_menu_panel(clickOn, screenDiffChecker):
    clickOn(btn.system_menu_panel)
    assert screenDiffChecker(
        'localization/zh_CN/set_system_menu_panel.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_system_mic_array(clickOn, screenDiffChecker):
    clickOn(btn.system_mic_array)
    assert screenDiffChecker(
        'localization/zh_CN/set_system_mic_array.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_system_reset(clickOn, screenDiffChecker):
    clickOn(btn.system_reset)
    assert screenDiffChecker(
        'localization/zh_CN/set_system_reset.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_applications(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.apps)
    assert screenDiffChecker(
        'localization/zh_CN/set_applications.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.fr)
    assert screenDiffChecker(
        'localization/zh_CN/set_face_recognize.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_fr_facedb(clickOn, screenDiffChecker):
    clickOn(btn.fr_facedb)
    assert screenDiffChecker(
        'localization/zh_CN/set_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_fr_adding_faces_modal(clickOn, screenDiffChecker):
    clickOn(btn.fr_facedb_select_folder)
    assert screenDiffChecker(
        'localization/zh_CN/set_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_navigation(clickOn, screenDiffChecker):
    clickOn(modal.add_faces_close)
    clickOn(btn.back)
    clickOn(btn.nav)
    assert screenDiffChecker(
        'localization/zh_CN/set_navigation.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_save_parameters(clickOn, screenDiffChecker):
    clickOn(params.useRadius)
    clickOn(params.useRadius)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    assert screenDiffChecker(
        'localization/zh_CN/set_save_parameters.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_lingvo(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.lingvo)
    assert screenDiffChecker(
        'localization/zh_CN/set_lingvo.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_lingvo_sources(clickOn, screenDiffChecker):
    clickOn(btn.lingvo_sources)
    assert screenDiffChecker(
        'localization/zh_CN/set_lingvo_sources.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_language_settings(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.lang_settings)
    assert screenDiffChecker(
        'localization/zh_CN/set_language_settings.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_internet_services(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.internet)
    assert screenDiffChecker(
        'localization/zh_CN/set_internet_services.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_internet_services_sip(clickOn, screenDiffChecker):
    clickOn(btn.internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/zh_CN/set_internet_services_sip.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_internet_services_ya_disk(clickOn, screenDiffChecker):
    clickOn(btn.internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/zh_CN/set_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_zh_CN
def test_update(clickOn, screenDiffChecker):
    clickOn(btn.back)
    time.sleep(default)
    clickOn(btn.update)
    assert screenDiffChecker(
        'localization/zh_CN/set_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_zh_CN
def test_reset(clickOn, typeText, node):
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lang_settings)
    for i in range(12):
        clickOn(btn.lang_down_arrow)
    clickOn(btn.lang_ru_RU)
    clickOn(btn.lang_set_default)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'ru_RU'
