#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

@pytest.mark.networkOff
def test_disconnect(clickOn):
    clickOn('control')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('connection')

# TODO
