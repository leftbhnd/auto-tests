#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
60.80 seconds
'''


@pytest.mark.appsMenu
def test_menu_open_button(clickOn, customScreenDiffChecker):
    clickOn('play')
    clickOn('radius_modal_yes')
    time.sleep(10)
    clickOn('apps_menu_open')
    assert customScreenDiffChecker(
        {'image': 'apps_menu.png', 'coordinates': (0, 40, 1280, 660)}
    ) is None


@pytest.mark.appsMenu
def test_menu_close_swipe(pressAndMove, customScreenDiffChecker):
    pressAndMove([(616, 62), (608, 734)])
    assert customScreenDiffChecker(
        {'image': 'gui.png', 'coordinates': (0, 40, 1280, 660)}
    ) is None


@pytest.mark.appsMenu
def test_menu_open_swipe(pressAndMove, customScreenDiffChecker):
    pressAndMove([(608, 734), (616, 62)])
    assert customScreenDiffChecker(
        {'image': 'apps_menu.png', 'coordinates': (0, 40, 1280, 660)}
    ) is None


@pytest.mark.appsMenu
def test_menu_close_button(clickOn, customScreenDiffChecker):
    clickOn('apps_menu_close')
    assert customScreenDiffChecker(
        {'image': 'gui.png', 'coordinates': (0, 40, 1280, 660)}
    ) is None


@pytest.mark.appsMenu
def test_restore(openPasswordModal, clickOn, typeText, screenDiffChecker):
    openPasswordModal()
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert screenDiffChecker('start.png') is None
