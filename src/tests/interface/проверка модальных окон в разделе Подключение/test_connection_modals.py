#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
23.99 seconds
'''


@pytest.mark.connection_modals
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


@pytest.mark.connection_modals
def test_connection_info_modal(clickOn, customScreenDiffChecker):
    clickOn('connection_info')
    time.sleep(5)
    assert customScreenDiffChecker(
        {
            'image': 'connection_info_modal.png',
            'coordinates': (365, 292, 548, 212)
        }
    ) is None


@pytest.mark.connection_modals
def test_connection_update_modal(clickOn, customScreenDiffChecker):
    clickOn('connection_info_modal_close')
    clickOn('connection_update')
    time.sleep(2)
    assert customScreenDiffChecker(
        {
            'image': 'connection_update_modal.png',
            'coordinates': (0, 40, 1280, 120)
        }
    ) is None


@pytest.mark.connection_modals
def test_connection_wifi_pass_modal(clickOn, customScreenDiffChecker):
    time.sleep(3)
    clickOn('random_wifi')
    clickOn('reset_input')
    clickOn('reset_input')
    assert customScreenDiffChecker(
        {
            'image': 'wifi_pass_modal.png',
            'coordinates': (365, 292, 548, 212)
        }
    ) is None


@pytest.mark.connection_modals
def test_reset(clickOn, screenDiffChecker):
    clickOn('wifi_pass_modal_close')
    clickOn('back')
    clickOn('back')
