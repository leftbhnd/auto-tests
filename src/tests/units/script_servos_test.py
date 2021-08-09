#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import pytest


def test_script(node):
    node.scriptProcessListener()
    assert node.getScriptProcess() == ['test_rotate_head', True]


def test_servos_state(node):
    node.servoStateListener()
    assert node.getServosState() is ''
