#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, running, restart
'''
115.68 seconds
'''


@pytest.mark.interface_statuses_of_running
def test_disable_radius(click, typeText, node):
    click(btn.start.control)
    typeText(123456)
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.nav)
    click(btn.nav.useRadius)
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.reset)
    click(btn.handler.back)
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    assert node.getUseRadius() == False


@pytest.mark.interface_statuses_of_running
def test_run_state(click, screenDiffChecker):
    click(btn.start.play)
    assert screenDiffChecker(
        'interfaces/run_state.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'interfaces/run_active.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'interfaces/run.png'
    ) is None


@pytest.mark.interface_statuses_of_running
def test_restore(click, openServiceMenu, node):
    time.sleep(running)
    openServiceMenu()
    click(btn.control.settings)
    click(btn.settings.nav)
    click(btn.nav.useRadius)
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.reset)
    click(btn.handler.back)
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    assert node.getUseRadius() == True
