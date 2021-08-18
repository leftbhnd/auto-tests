#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.skip(reason="units")
def test_script(node):
    assert node.getScriptProcess() == ['test_rotate_head', True]


@pytest.mark.skip(reason="units")
def test_servos_state(node):
    assert node.getServosState() is ''
