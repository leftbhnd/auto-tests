#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, param, interaction
'''
183.89 seconds
'''


@pytest.mark.interaction_interaction
def test_activate_speech(click, openServiceMenu, db):
    db.updateValue([
        {'name': param.interaction.startByFace, 'value': 0},
        {'name': param.interaction.updateByFace, 'value': 0}
    ])
    openServiceMenu()
    click(btn.handler.back)
    time.sleep(interaction)


@pytest.mark.interaction_interaction
def test_start_by_speech(node):
    node.asrPub('привет')
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_interaction
def test_update_by_speech(node):
    time.sleep(10)
    in_interaction = node.getInteraction()
    node.asrPub('как дела?')
    time.sleep(10)
    assert node.getInteraction() == in_interaction


@pytest.mark.interaction_interaction
def test_start_by_face_disabled(node):
    time.sleep(interaction)
    node.facePub(3, 0, 0, 3, 1.0)
    node.clearFacePub()
    assert node.getInteraction() == [False, 0]


@pytest.mark.interaction_interaction
def test_activate_face(click, openServiceMenu, db):
    db.updateValue([
        {'name': param.interaction.startByFace, 'value': 1},
        {'name': param.interaction.updateByFace, 'value': 1},
        {'name': param.interaction.startBySpeech, 'value': 0},
        {'name': param.interaction.updateBySpeech, 'value': 0}
    ])
    openServiceMenu()
    click(btn.handler.back)
    time.sleep(interaction)


@pytest.mark.interaction_interaction
def test_start_by_face(node):
    node.facePub(3, 1, 0, 3, 1.0)
    node.clearFacePub()
    assert node.getInteraction() == [True, 1]


@pytest.mark.interaction_interaction
def test_update_by_face(node):
    time.sleep(10)
    in_interaction = node.getInteraction()
    node.facePub(3, 2, 0, 3, 1.0)
    node.clearFacePub()
    time.sleep(10)
    assert node.getInteraction() == in_interaction


@pytest.mark.interaction_interaction
def test_start_by_speech_disabled(node):
    time.sleep(interaction)
    node.asrPub('привет')
    assert node.getInteraction() == [False, 1]


@pytest.mark.interaction_interaction
def test_restore(click, openServiceMenu, db):
    db.updateValue([
        {'name': param.interaction.startByFace, 'value': 1},
        {'name': param.interaction.updateByFace, 'value': 1},
        {'name': param.interaction.startBySpeech, 'value': 1},
        {'name': param.interaction.updateBySpeech, 'value': 1}
    ])
    openServiceMenu()
    click(btn.handler.back)
    time.sleep(interaction)
