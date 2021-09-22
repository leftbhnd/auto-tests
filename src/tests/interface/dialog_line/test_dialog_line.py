#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.messages import AsrTtsMsg
from src.helpers.config import running, restart, btn, modal
'''
63.23 seconds
'''


@pytest.mark.interface_dialog_line
def test_dialog_line(clickOn, node, screenDiffChecker):
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('тестовое правило с лопатой')
    node.asrPub(asr_msg)
    assert screenDiffChecker(
        'interfaces/dialog_line.png'
    ) is None


@pytest.mark.interface_dialog_line
def test_restore(clickOn, openServiceMenu):
    openServiceMenu()
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
