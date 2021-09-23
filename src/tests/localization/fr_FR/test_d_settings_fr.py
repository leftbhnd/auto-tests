#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, btn, modal, params
'''
32.65 seconds
'''


@pytest.mark.localization_fr_FR
def test_settings(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.settings)
    assert screenDiffChecker(
        'localization/fr_FR/settings.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_system(click, screenDiffChecker):
    click(btn.system)
    assert screenDiffChecker(
        'localization/fr_FR/set_system.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_system_interaction(click, screenDiffChecker):
    click(btn.system_interaction)
    assert screenDiffChecker(
        'localization/fr_FR/set_system_interaction.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_system_menu_panel(click, screenDiffChecker):
    click(btn.system_menu_panel)
    assert screenDiffChecker(
        'localization/fr_FR/set_system_menu_panel.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_system_mic_array(click, screenDiffChecker):
    click(btn.system_mic_array)
    assert screenDiffChecker(
        'localization/fr_FR/set_system_mic_array.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_system_reset(click, screenDiffChecker):
    click(btn.system_reset)
    assert screenDiffChecker(
        'localization/fr_FR/set_system_reset.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_applications(click, screenDiffChecker):
    click(btn.back)
    click(btn.apps)
    assert screenDiffChecker(
        'localization/fr_FR/set_applications.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_face_recognize(click, screenDiffChecker):
    click(btn.back)
    click(btn.fr)
    assert screenDiffChecker(
        'localization/fr_FR/set_face_recognize.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_fr_facedb(click, screenDiffChecker):
    click(btn.fr_facedb)
    assert screenDiffChecker(
        'localization/fr_FR/set_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_fr_adding_faces_modal(click, screenDiffChecker):
    click(btn.fr_facedb_select_folder)
    assert screenDiffChecker(
        'localization/fr_FR/set_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_navigation(click, screenDiffChecker):
    click(modal.add_faces_close)
    click(btn.back)
    click(btn.nav)
    assert screenDiffChecker(
        'localization/fr_FR/set_navigation.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_save_parameters(click, screenDiffChecker):
    click(params.useRadius)
    click(params.useRadius)
    click(btn.back)
    click(modal.save_yes)
    assert screenDiffChecker(
        'localization/fr_FR/set_save_parameters.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_lingvo(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.lingvo)
    assert screenDiffChecker(
        'localization/fr_FR/set_lingvo.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_lingvo_sources(click, screenDiffChecker):
    click(btn.lingvo_sources)
    assert screenDiffChecker(
        'localization/fr_FR/set_lingvo_sources.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_language_settings(click, screenDiffChecker):
    click(btn.back)
    click(btn.lang_settings)
    assert screenDiffChecker(
        'localization/fr_FR/set_language_settings.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_internet_services(click, screenDiffChecker):
    click(btn.back)
    click(btn.internet)
    assert screenDiffChecker(
        'localization/fr_FR/set_internet_services.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_internet_services_sip(click, screenDiffChecker):
    click(btn.internet_sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/fr_FR/set_internet_services_sip.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_internet_services_ya_disk(click, screenDiffChecker):
    click(btn.internet_ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/fr_FR/set_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_fr_FR
def test_update(click, screenDiffChecker):
    click(btn.back)
    time.sleep(default)
    click(btn.update)
    assert screenDiffChecker(
        'localization/fr_FR/set_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_fr_FR
def test_reset(click):
    click(btn.back)
    click(btn.back)
    click(btn.back)
    time.sleep(modals)
