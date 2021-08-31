#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.skip(reason="unit")
def test_script(node):
    node.initNode()
    assert node.getScriptProcess() == ['test_rotate_head', True]


@pytest.mark.skip(reason="unit")
def test_servos_state(node):
    assert node.getServosState() is ''


@pytest.mark.skip(reason="unit")
def test_finish(node):
    node.killNode()
