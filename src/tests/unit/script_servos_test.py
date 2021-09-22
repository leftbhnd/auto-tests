#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.unit
def test_script(node):
    assert node.getScriptProcess() == [True, 'test_rotate_head']


@pytest.mark.unit
def test_servos_state(node):
    assert node.getServosState() is ''
