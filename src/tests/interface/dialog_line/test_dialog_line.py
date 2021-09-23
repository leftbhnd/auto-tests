#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import running, restart, btn, modal
'''
63.23 seconds
'''


@pytest.mark.interface_dialog_line
def test_dialog_line(click, node, screenDiffChecker):
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    node.cancelSpeechPub()
    node.asrPub('тестовое правило с лопатой')
    assert screenDiffChecker(
        'interfaces/dialog_line.png'
    ) is None


@pytest.mark.interface_dialog_line
def test_restore(click, openServiceMenu):
    openServiceMenu()
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
