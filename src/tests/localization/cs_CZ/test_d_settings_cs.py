#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, param, default, slowly, modals
'''
X seconds
'''


@pytest.mark.localization_cs_CZ
def test_settings(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.settings)
    assert screenDiffChecker(
        'localization/cs_CZ/settings.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system(click, screenDiffChecker):
    click(btn.settings.system)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system_interaction(click, screenDiffChecker):
    click(btn.system.interaction)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system_interaction.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system_menu_panel(click, screenDiffChecker):
    click(btn.system.menu_panel)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system_menu_panel.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system_mic_array(click, screenDiffChecker):
    click(btn.system.mic_array)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system_mic_array.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_system_reset(click, screenDiffChecker):
    click(btn.system.reset)
    assert screenDiffChecker(
        'localization/cs_CZ/set_system_reset.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_applications(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.apps)
    assert screenDiffChecker(
        'localization/cs_CZ/set_applications.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_face_recognize(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.fr)
    assert screenDiffChecker(
        'localization/cs_CZ/set_face_recognize.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_fr_facedb(click, screenDiffChecker):
    click(btn.fr.facedb)
    assert screenDiffChecker(
        'localization/cs_CZ/set_face_recognize_facedb.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_fr_adding_faces_modal(click, screenDiffChecker):
    click(btn.fr.facedb_select_folder)
    assert screenDiffChecker(
        'localization/cs_CZ/set_adding_faces_modal.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_navigation(click, screenDiffChecker):
    click(modal.add_face.close)
    click(btn.handler.back)
    click(btn.settings.nav)
    assert screenDiffChecker(
        'localization/cs_CZ/set_navigation.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_save_parameters(click, screenDiffChecker):
    click(param.driving.useRadius)
    click(param.driving.useRadius)
    click(btn.handler.back)
    click(modal.save.yes)
    assert screenDiffChecker(
        'localization/cs_CZ/set_save_parameters.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_lingvo(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.settings.lingvo)
    assert screenDiffChecker(
        'localization/cs_CZ/set_lingvo.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_lingvo_sources(click, screenDiffChecker):
    click(btn.lingvo.sources)
    assert screenDiffChecker(
        'localization/cs_CZ/set_lingvo_sources.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_language_settings(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.lang)
    assert screenDiffChecker(
        'localization/cs_CZ/set_language_settings.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_internet_services(click, screenDiffChecker):
    click(btn.handler.back)
    click(btn.settings.internet)
    assert screenDiffChecker(
        'localization/cs_CZ/set_internet_services.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_internet_services_sip(click, screenDiffChecker):
    click(btn.internet.sip)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/cs_CZ/set_internet_services_sip.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_internet_services_ya_disk(click, screenDiffChecker):
    click(btn.internet.ya_disk)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/cs_CZ/set_internet_services_ya_disk.png'
    ) is None


@pytest.mark.localization_cs_CZ
def test_update(click, screenDiffChecker):
    click(btn.handler.back)
    time.sleep(default)
    click(btn.settings.update)
    assert screenDiffChecker(
        'localization/cs_CZ/set_update.png',
        (0, 215, 1280, 585)
    ) is None


@pytest.mark.localization_cs_CZ
def test_reset(click):
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(modals)
