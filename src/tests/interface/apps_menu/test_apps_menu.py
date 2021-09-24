#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, default, running, restart
'''
65.54 seconds
'''


@pytest.mark.interface_apps_menu
def test_menu_open_button(click, screenDiffChecker):
    click(btn.start.play)
    click(modal.radius.yes)
    time.sleep(running)
    click(btn.gui.apps_menu_open)
    time.sleep(default)
    assert screenDiffChecker(
        'interfaces/apps_menu.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interface_apps_menu
def test_menu_close_swipe(dNd, screenDiffChecker):
    dNd((616, 62), (608, 734))
    time.sleep(default)
    assert screenDiffChecker(
        'interfaces/gui.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interface_apps_menu
def test_menu_open_swipe(dNd, screenDiffChecker):
    dNd((608, 734), (616, 62))
    time.sleep(default)
    assert screenDiffChecker(
        'interfaces/apps_menu.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interface_apps_menu
def test_menu_close_button(click, screenDiffChecker):
    click(btn.gui.apps_menu_close)
    time.sleep(default)
    assert screenDiffChecker(
        'interfaces/gui.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interface_apps_menu
def test_restore(click, openServiceMenu):
    openServiceMenu()
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
