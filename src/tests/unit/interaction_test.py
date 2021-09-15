#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from src.helpers.messages import InteractionMsg

# reason's type: Speech = 0, Face = 1, Click = 2, Hark = 3


@pytest.mark.skip(reason="unit")
def test_interaction_speech_true(node):
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [True, 0]


@pytest.mark.skip(reason="unit")
def test_interaction_speech_false(node):
    interaction_msg = InteractionMsg(False, 0)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [False, 0]


@pytest.mark.skip(reason="unit")
def test_interaction_face_true(node):
    interaction_msg = InteractionMsg(True, 1)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [True, 1]


@pytest.mark.skip(reason="unit")
def test_interaction_face_false(node):
    interaction_msg = InteractionMsg(False, 1)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [False, 1]


@pytest.mark.skip(reason="unit")
def test_interaction_click_true(node):
    interaction_msg = InteractionMsg(True, 2)
    node.interactionPub(interaction_msg)
    #node.interactionPub(True, 2)
    assert node.getInteraction() == [True, 2]


@pytest.mark.skip(reason="unit")
def test_interaction_click_false(node):
    interaction_msg = InteractionMsg(False, 2)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [False, 2]


@pytest.mark.skip(reason="unit")
def test_interaction_hark_true(node):
    interaction_msg = InteractionMsg(True, 3)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [True, 3]


@pytest.mark.skip(reason="unit")
def test_interaction_hark_false(node):
    interaction_msg = InteractionMsg(False, 3)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [False, 3]
