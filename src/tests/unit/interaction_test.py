#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# reason's type: Speech = 0, Face = 1, Click = 2, Hark = 3


@pytest.mark.skip(reason="unit")
def test_interaction_speech_true(node):
    node.interactionPub(True, 0)
    assert node.getInteraction() == [True, 0]


@pytest.mark.skip(reason="unit")
def test_interaction_speech_false(node):
    node.interactionPub(False, 0)
    assert node.getInteraction() == [False, 0]


@pytest.mark.skip(reason="unit")
def test_interaction_face_true(node):
    node.interactionPub(True, 1)
    assert node.getInteraction() == [True, 1]


@pytest.mark.skip(reason="unit")
def test_interaction_face_false(node):
    node.interactionPub(False, 1)
    assert node.getInteraction() == [False, 1]


@pytest.mark.skip(reason="unit")
def test_interaction_click_true(node):
    node.interactionPub(True, 2)
    assert node.getInteraction() == [True, 2]


@pytest.mark.skip(reason="unit")
def test_interaction_click_false(node):
    node.interactionPub(False, 2)
    assert node.getInteraction() == [False, 2]


@pytest.mark.skip(reason="unit")
def test_interaction_hark_true(node):
    node.interactionPub(True, 3)
    assert node.getInteraction() == [True, 3]


@pytest.mark.skip(reason="unit")
def test_interaction_hark_false(node):
    node.interactionPub(False, 3)
    assert node.getInteraction() == [False, 3]
