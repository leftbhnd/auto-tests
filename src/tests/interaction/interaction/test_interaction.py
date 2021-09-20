#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time
import rospy

from src.helpers.config import btn, modal, params, modals, interaction
from src.helpers.messages import FaceMsg, AsrTtsMsg
'''
X seconds
'''
rospy.init_node('autotest')
node = AutoTest()

@pytest.mark.interaction_interaction
def test_activate_speech(openPwdModal, typeText, clickOn):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
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
def test_start_by_speech():
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('привет')
    node.asrPub(asr_msg)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_interaction
def test_clear_interaction_start_by_speech():
    node.cancelSpeechPub()
    time.sleep(interaction)
    assert node.getInteraction() == [False, 0]


@pytest.mark.interaction_interaction
def test_setup_update_by_speech():
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('привет')
    node.asrPub(asr_msg)
    node.cancelSpeechPub()
    time.sleep(5)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_interaction
def test_update_by_speech():
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('как дела?')
    node.asrPub(asr_msg)
    node.cancelSpeechPub()
    time.sleep(5)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_interaction
def test_start_by_face_disabled():
    node.cancelSpeechPub()
    time.sleep(interaction)
    face_msg = FaceMsg(2, False, 22, 228, 0.9)
    node.facePub(face_msg)
    assert node.getInteraction() == [False, 0]


@pytest.mark.interaction_interaction
def test_activate_face(openPwdModal, typeText, clickOn):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
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
def test_start_by_face():
    face_msg = FaceMsg(2, False, 23, 229, 0.9)
    node.facePub(face_msg)
    assert node.getInteraction() == [True, 1]


@pytest.mark.interaction_interaction
def test_clear_interaction_start_by_face():
    node.cancelSpeechPub()
    time.sleep(interaction)
    assert node.getInteraction() == [False, 1]


@pytest.mark.interaction_interaction
def test_setup_update_by_face():
    node.cancelSpeechPub()
    face_msg = FaceMsg(2, False, 24, 230, 0.9)
    node.facePub(face_msg)
    time.sleep(5)
    assert node.getInteraction() == [True, 1]


@pytest.mark.interaction_interaction
def test_update_by_face():
    node.cancelSpeechPub()
    face_msg = FaceMsg(2, False, 25, 231, 0.9)
    node.facePub(face_msg)
    time.sleep(5)
    assert node.getInteraction() == [True, 1]


@pytest.mark.interaction_interaction
def test_start_by_speech_disabled():
    node.cancelSpeechPub()
    time.sleep(interaction)
    asr_msg = AsrTtsMsg('привет')
    node.asrPub(asr_msg)
    assert node.getInteraction() == [False, 1]


@pytest.mark.interaction_interaction
def test_restore(openPwdModal, typeText, clickOn):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
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
