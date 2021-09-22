#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, params, modals, interaction
'''
249.59 seconds
'''


@pytest.mark.interaction_interaction
def test_activate_speech(click, openServiceMenu):
    openServiceMenu()
    click(btn.settings)
    click(btn.system)
    click(btn.system_interaction)
    for i in range(19):
        click(btn.system_interaction_down_arrow)
    click(params.startByFace)
    click(params.startByFaceDisable)
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.back)
    time.sleep(interaction)


@pytest.mark.interaction_interaction
def test_start_by_speech(node):
    node.cancelSpeechPub()
    node.asrPub('привет')
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_interaction
def test_clear_interaction_start_by_speech(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
    assert node.getInteraction() == [False, 0]


@pytest.mark.interaction_interaction
def test_setup_update_by_speech(node):
    node.cancelSpeechPub()
    node.asrPub('привет')
    node.cancelSpeechPub()
    time.sleep(5)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_interaction
def test_update_by_speech(node):
    node.cancelSpeechPub()
    node.asrPub('привет')
    node.cancelSpeechPub()
    time.sleep(10)
    in_interaction = node.getInteraction()
    node.asrPub('как дела?')
    node.cancelSpeechPub()
    time.sleep(10)
    assert node.getInteraction() == in_interaction


@pytest.mark.interaction_interaction
def test_start_by_face_disabled(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getInteraction() == [False, 0]


@pytest.mark.interaction_interaction
def test_activate_face(click, openServiceMenu, node):
    node.clearFacePub()
    openServiceMenu()
    click(btn.settings)
    click(btn.system)
    click(btn.system_interaction)
    click(params.startBySpeech)
    click(params.startBySpeechDisable)
    click(params.updateBySpeech)
    click(params.updateBySpeechDisable)
    for i in range(19):
        click(btn.system_interaction_down_arrow)
    click(params.startByFace)
    click(params.startByFaceEnable)
    click(params.updateByFace)
    click(params.updateByFaceEnable)
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.back)
    time.sleep(interaction)


@pytest.mark.interaction_interaction
def test_start_by_face(node):
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getInteraction() == [True, 1]


@pytest.mark.interaction_interaction
def test_clear_interaction_start_by_face(node):
    node.clearFacePub()
    node.cancelSpeechPub()
    time.sleep(interaction)
    assert node.getInteraction() == [False, 1]


@pytest.mark.interaction_interaction
def test_setup_update_by_face(node):
    node.clearFacePub()
    node.cancelSpeechPub()
    node.facePub(3, 0, 0, 3, 1.0)
    node.clearFacePub()
    time.sleep(5)
    assert node.getInteraction() == [True, 1]


@pytest.mark.interaction_interaction
def test_update_by_face(node):
    node.cancelSpeechPub()
    node.facePub(3, 0, 0, 3, 1.0)
    node.clearFacePub()
    node.cancelSpeechPub()
    time.sleep(10)
    in_interaction = node.getInteraction()
    node.facePub(3, 0, 0, 3, 1.0)
    node.clearFacePub()
    time.sleep(10)
    assert node.getInteraction() == in_interaction


@pytest.mark.interaction_interaction
def test_start_by_speech_disabled(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
    node.asrPub('привет')
    assert node.getInteraction() == [False, 1]


@pytest.mark.interaction_interaction
def test_restore(click, openServiceMenu):
    openServiceMenu()
    click(btn.settings)
    click(btn.system)
    click(btn.system_interaction)
    click(params.startBySpeech)
    click(params.startBySpeechEnable)
    click(params.updateBySpeech)
    click(params.updateBySpeechEnable)
    for i in range(19):
        click(btn.system_interaction_down_arrow)
    click(params.startByFace)
    click(params.startByFaceEnable)
    click(params.updateByFace)
    click(params.updateByFaceDisable)
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.back)
    time.sleep(interaction)
