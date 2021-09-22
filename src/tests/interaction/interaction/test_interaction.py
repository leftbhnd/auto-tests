#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, params, modals, interaction
from src.helpers.messages import AsrTtsMsg
'''
249.59 seconds
'''


@pytest.mark.interaction_interaction
def test_activate_speech(clickOn, openServiceMenu):
    openServiceMenu()
    clickOn(btn.settings)
    clickOn(btn.system)
    clickOn(btn.system_interaction)
    for i in range(19):
        clickOn(btn.system_interaction_down_arrow)
    clickOn(params.startByFace)
    clickOn(params.startByFaceDisable)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(interaction)


@pytest.mark.interaction_interaction
def test_start_by_speech(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('привет')
    node.asrPub(asr_msg)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_interaction
def test_clear_interaction_start_by_speech(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
    assert node.getInteraction() == [False, 0]


@pytest.mark.interaction_interaction
def test_setup_update_by_speech(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('привет')
    node.asrPub(asr_msg)
    node.cancelSpeechPub()
    time.sleep(5)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_interaction
def test_update_by_speech(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('привет')
    node.asrPub(asr_msg)
    node.cancelSpeechPub()
    time.sleep(10)
    in_interaction = node.getInteraction()
    asr_msg = AsrTtsMsg('как дела?')
    node.asrPub(asr_msg)
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
def test_activate_face(clickOn, openServiceMenu, node):
    node.clearFacePub()
    openServiceMenu()
    clickOn(btn.settings)
    clickOn(btn.system)
    clickOn(btn.system_interaction)
    clickOn(params.startBySpeech)
    clickOn(params.startBySpeechDisable)
    clickOn(params.updateBySpeech)
    clickOn(params.updateBySpeechDisable)
    for i in range(19):
        clickOn(btn.system_interaction_down_arrow)
    clickOn(params.startByFace)
    clickOn(params.startByFaceEnable)
    clickOn(params.updateByFace)
    clickOn(params.updateByFaceEnable)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
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
    asr_msg = AsrTtsMsg('привет')
    node.asrPub(asr_msg)
    assert node.getInteraction() == [False, 1]


@pytest.mark.interaction_interaction
def test_restore(clickOn, openServiceMenu):
    openServiceMenu()
    clickOn(btn.settings)
    clickOn(btn.system)
    clickOn(btn.system_interaction)
    clickOn(params.startBySpeech)
    clickOn(params.startBySpeechEnable)
    clickOn(params.updateBySpeech)
    clickOn(params.updateBySpeechEnable)
    for i in range(19):
        clickOn(btn.system_interaction_down_arrow)
    clickOn(params.startByFace)
    clickOn(params.startByFaceEnable)
    clickOn(params.updateByFace)
    clickOn(params.updateByFaceDisable)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(interaction)
