#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, param, modals, interaction
'''
191.12 seconds
'''


@pytest.mark.interaction_interaction
def test_activate_speech(click, openServiceMenu):
    openServiceMenu()
    click(btn.control.settings)
    click(btn.settings.system)
    click(btn.system.interaction)
    for i in range(19):
        click(btn.handler.interaction_down_arr)
    click(param.interaction.startByFace)
    click(param.interaction.startByFaceDisable)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(interaction)


@pytest.mark.interaction_interaction
def test_start_by_speech(node):
    node.cancelSpeechPub()
    node.asrPub('привет')
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_interaction
def test_update_by_speech(node):
    node.cancelSpeechPub()
    time.sleep(10)
    in_interaction = node.getInteraction()
    node.asrPub('как дела?')
    node.cancelSpeechPub()
    time.sleep(10)
    assert node.getInteraction() == in_interaction


@pytest.mark.interaction_interaction
def test_start_by_face_disabled(node):
    time.sleep(interaction)
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getInteraction() == [False, 0]


@pytest.mark.interaction_interaction
def test_activate_face(click, openServiceMenu, node):
    node.clearFacePub()
    openServiceMenu()
    click(btn.control.settings)
    click(btn.settings.system)
    click(btn.system.interaction)
    click(param.interaction.startBySpeech)
    click(param.interaction.startBySpeechDisable)
    click(param.interaction.updateBySpeech)
    click(param.interaction.updateBySpeechDisable)
    for i in range(19):
        click(btn.handler.interaction_down_arr)
    click(param.interaction.startByFace)
    click(param.interaction.startByFaceEnable)
    click(param.interaction.updateByFace)
    click(param.interaction.updateByFaceEnable)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(interaction)


@pytest.mark.interaction_interaction
def test_start_by_face(node):
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getInteraction() == [True, 1]


@pytest.mark.interaction_interaction
def test_update_by_face(node):
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
    click(btn.control.settings)
    click(btn.settings.system)
    click(btn.system.interaction)
    click(param.interaction.startBySpeech)
    click(param.interaction.startBySpeechEnable)
    click(param.interaction.updateBySpeech)
    click(param.interaction.updateBySpeechEnable)
    for i in range(19):
        click(btn.handler.interaction_down_arr)
    click(param.interaction.startByFace)
    click(param.interaction.startByFaceEnable)
    click(param.interaction.updateByFace)
    click(param.interaction.updateByFaceDisable)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(interaction)
