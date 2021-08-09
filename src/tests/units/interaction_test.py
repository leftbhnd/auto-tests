#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.messages import InteractionMsg

# reason's type: Speech = 0, Face = 1, Click = 2, Hark = 3


def test_interaction_speech_true(node):
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    node.interactionListener()
    assert node.getInteraction() is [True, 0]


def test_interaction_speech_false(node):
    interaction_msg = InteractionMsg(False, 0)
    node.interactionPub(interaction_msg)
    node.interactionListener()
    assert node.getInteraction() is [False, 0]


def test_interaction_face_true(node):
    interaction_msg = InteractionMsg(True, 1)
    node.interactionPub(interaction_msg)
    node.interactionListener()
    assert node.getInteraction() is [True, 1]


def test_interaction_face_false(node):
    interaction_msg = InteractionMsg(False, 1)
    node.interactionPub(interaction_msg)
    node.interactionListener()
    assert node.getInteraction() is [False, 1]


def test_interaction_click_true(node):
    interaction_msg = InteractionMsg(True, 2)
    node.interactionPub(interaction_msg)
    node.interactionListener()
    assert node.getInteraction() is [True, 2]


def test_interaction_click_false(node):
    interaction_msg = InteractionMsg(False, 2)
    node.interactionPub(interaction_msg)
    node.interactionListener()
    assert node.getInteraction() is [False, 2]


def test_interaction_hark_true(node):
    interaction_msg = InteractionMsg(True, 3)
    node.interactionPub(interaction_msg)
    node.interactionListener()
    assert node.getInteraction() is [True, 3]


def test_interaction_hark_false(node):
    interaction_msg = InteractionMsg(False, 3)
    node.interactionPub(interaction_msg)
    node.interactionListener()
    assert node.getInteraction() is [False, 3]
