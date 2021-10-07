#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly, interaction
'''
X seconds
'''


@pytest.mark.navigation_interaction
def test_start_face_in_driving(node):
    node.autoModePub()
    while node.getDrivePause() != False:
        time.sleep(slowly)
    time.sleep(5)
    node.facePub(3, 0, 0, 3, 1.0)
    node.clearFacePub()
    assert node.getInteraction() == [True, 1]


@pytest.mark.navigation_interaction
def test_update_face_in_driving(node):
    time.sleep(10)
    in_interaction = node.getInteraction()
    node.facePub(3, 1, 0, 3, 1.0)
    node.clearFacePub()
    time.sleep(10)
    assert node.getInteraction() == in_interaction


@pytest.mark.navigation_interaction
def test_face_continue_driving(node):
    time.sleep(interaction - 10)
    assert node.getDrivePause() == False


@pytest.mark.navigation_interaction
def test_start_face_at_point(node):
    while node.getCurrentPoint() != 1:
        time.sleep(slowly)
    node.facePub(3, 2, 0, 3, 1.0)
    node.clearFacePub()
    assert node.getInteraction() == [True, 1]


@pytest.mark.navigation_interaction
def test_update_face_at_point(node):
    time.sleep(10)
    in_interaction = node.getInteraction()
    node.facePub(3, 3, 0, 3, 1.0)
    node.clearFacePub()
    time.sleep(10)
    assert node.getInteraction() == in_interaction


@pytest.mark.navigation_interaction
def test_reset(node):
    node.chargeAppPub()
    time.sleep(60)
    assert node.getChargeState() == True
