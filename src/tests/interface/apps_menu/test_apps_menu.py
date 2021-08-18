#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.messages import SwipeMsg
from src.helpers.test_config import running_timeout, restart_timeout
'''
60.80 seconds
'''


@pytest.mark.interface
def test_menu_open_button(clickOn, screenDiffChecker):
    clickOn('play')
    clickOn('radius_modal_yes')
    time.sleep(running_timeout)
    clickOn('apps_menu_open')
    assert screenDiffChecker('apps_menu.png', (0, 40, 1280, 660)) is None


@pytest.mark.interface
def test_menu_close_swipe(pressAndMove, screenDiffChecker):
    swipe_msg = SwipeMsg((616, 62), (608, 734))
    pressAndMove(swipe_msg)
    assert screenDiffChecker('gui.png', (0, 40, 1280, 660)) is None


@pytest.mark.interface
def test_menu_open_swipe(pressAndMove, screenDiffChecker):
    swipe_msg = SwipeMsg((608, 734), (616, 62))
    pressAndMove(swipe_msg)
    assert screenDiffChecker(
        'apps_menu.png', (0, 40, 1280, 660)) is None


@pytest.mark.interface
def test_menu_close_button(clickOn, screenDiffChecker):
    clickOn('apps_menu_close')
    assert screenDiffChecker('gui.png', (0, 40, 1280, 660)) is None


@pytest.mark.interface
def test_restore(openPasswordModal, clickOn, typeText, screenDiffChecker):
    openPasswordModal()
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(restart_timeout)
    assert screenDiffChecker('start.png') is None
