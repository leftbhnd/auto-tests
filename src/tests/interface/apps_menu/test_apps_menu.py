#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.messages import SwipeMsg
from src.helpers.config import default, running, restart, btn, modal
'''
65.54 seconds
'''


@pytest.mark.interface_apps_menu
def test_menu_open_button(clickOn, screenDiffChecker):
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    clickOn(btn.apps_menu_open)
    time.sleep(default)
    assert screenDiffChecker(
        'interfaces/apps_menu.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interface_apps_menu
def test_menu_close_swipe(pressAndMove, screenDiffChecker):
    swipe_msg = SwipeMsg((616, 62), (608, 734))
    pressAndMove(swipe_msg)
    time.sleep(default)
    assert screenDiffChecker(
        'interfaces/gui.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interface_apps_menu
def test_menu_open_swipe(pressAndMove, screenDiffChecker):
    swipe_msg = SwipeMsg((608, 734), (616, 62))
    pressAndMove(swipe_msg)
    time.sleep(default)
    assert screenDiffChecker(
        'interfaces/apps_menu.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interface_apps_menu
def test_menu_close_button(clickOn, screenDiffChecker):
    clickOn(btn.apps_menu_close)
    time.sleep(default)
    assert screenDiffChecker(
        'interfaces/gui.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interface_apps_menu
def test_restore(openPasswordModal, clickOn, typeText, screenDiffChecker):
    openPasswordModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
