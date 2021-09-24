#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, running, restart
'''
63.23 seconds
'''


@pytest.mark.interface_dialog_line
def test_dialog_line(click, screenDiffChecker, node):
    click(btn.start.play)
    click(modal.radius.yes)
    time.sleep(running)
    node.cancelSpeechPub()
    node.asrPub('тестовое правило с лопатой')
    assert screenDiffChecker(
        'interfaces/dialog_line.png'
    ) is None


@pytest.mark.interface_dialog_line
def test_restore(click, openServiceMenu):
    openServiceMenu()
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
