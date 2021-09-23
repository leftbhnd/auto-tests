#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal, params
'''
X seconds
'''


@pytest.mark.localization_cs_CZ
def test_settings(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.settings)
    assert screenDiffChecker(
        'localization/cs_CZ/settings.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system(click, type, screenDiffChecker):
    click(btn.system)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system_interaction(click, screenDiffChecker):
    click(btn.system_interaction)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system_interaction.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system_menu_panel(click, screenDiffChecker):
    click(btn.system_menu_panel)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system_menu_panel.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system_mic_array(click, screenDiffChecker):
    click(btn.system_mic_array)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system_mic_array.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system_reset(click, screenDiffChecker):
    click(btn.system_reset)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system_reset.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_applications(click, screenDiffChecker):
    click(btn.back)
    click(btn.apps)
    assert screenDiffChecker(
        'localization/cs_CZ/set_applications.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_face_recognize(click, screenDiffChecker):
    click(btn.back)
    click(btn.fr)
    assert screenDiffChecker(
        'localization/cs_CZ/set_face_recognize.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_fr_facedb(click, screenDiffChecker):
    click(btn.fr_facedb)
    assert screenDiffChecker(
        'localization/cs_CZ/set_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_fr_adding_faces_modal(click, screenDiffChecker):
    click(btn.fr_facedb_select_folder)
    assert screenDiffChecker(
        'localization/cs_CZ/set_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_navigation(click, screenDiffChecker):
    click(modal.add_faces_close)
    click(btn.back)
    click(btn.nav)
    assert screenDiffChecker(
        'localization/cs_CZ/set_navigation.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_save_parameters(click, screenDiffChecker):
    click(params.useRadius)
    click(params.useRadius)
    click(btn.back)
    click(modal.save_yes)
    assert screenDiffChecker(
        'localization/cs_CZ/set_save_parameters.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_lingvo(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.lingvo)
    assert screenDiffChecker(
        'localization/cs_CZ/set_lingvo.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_lingvo_sources(click, screenDiffChecker):
    click(btn.lingvo_sources)
    assert screenDiffChecker(
        'localization/cs_CZ/set_lingvo_sources.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_language_settings(click, screenDiffChecker):
    click(btn.back)
    click(btn.lang_settings)
    assert screenDiffChecker(
        'localization/cs_CZ/set_language_settings.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_internet_services(click, screenDiffChecker):
    click(btn.back)
    click(btn.internet)
    assert screenDiffChecker(
        'localization/cs_CZ/set_internet_services.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_internet_services_sip(click, screenDiffChecker):
    click(btn.internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/cs_CZ/set_internet_services_sip.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_internet_services_ya_disk(click, screenDiffChecker):
    click(btn.internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/cs_CZ/set_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_update(click, screenDiffChecker):
    click(btn.back)
    time.sleep(default)
    click(btn.update)
    assert screenDiffChecker(
        'localization/cs_CZ/set_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_cs_CZ
def test_reset(click):
    click(btn.back)
    click(btn.back)
    click(btn.back)
    time.sleep(modals)
