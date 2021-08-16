#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
58.57 seconds
'''


@pytest.mark.wifi_input
def test_connection_open(clickOn, typeText, customScreenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('connection')
    time.sleep(5)
    assert customScreenDiffChecker(
        {
            'image': 'connection.png', 'coordinates': (0, 40, 920, 150)
        }
    ) is None


@pytest.mark.wifi_input
def test_hide_input(clickOn, typeText, customScreenDiffChecker):
    time.sleep(3)
    clickOn('random_wifi')
    clickOn('wifi_pass_modal_input')
    clickOn('choose_numbers')
    typeText(['2', '2', '8', '1', '4', '8', '8'])
    clickOn('reset_input')
    clickOn('reset_input')
    assert customScreenDiffChecker(
        {
            'image': 'wifi_hide_pass.png',
            'coordinates': (365, 162, 548, 200)
        }
    ) is None


@pytest.mark.wifi_input
def test_visiable_input(clickOn, customScreenDiffChecker):
    clickOn('kb_wifi_pass_modal_eye')
    clickOn('reset_input')
    clickOn('reset_input')
    assert customScreenDiffChecker(
        {
            'image': 'wifi_visiable_pass.png',
            'coordinates': (365, 162, 548, 200)
        }
    ) is None


@pytest.mark.wifi_input
def test_reset(clickOn, screenDiffChecker):
    clickOn('kb_wifi_pass_modal_close')
    clickOn('back')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert screenDiffChecker('start.png') is None
