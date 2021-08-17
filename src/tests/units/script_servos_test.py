#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import pytest


def test_script(node):
    assert node.getScriptProcess() == ['test_rotate_head', True]


def test_servos_state(node):
    assert node.getServosState() is ''
