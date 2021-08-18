#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time
import uuid

from src.helpers.messages import AsrTtsMsg
from src.helpers.test_config import running_timeout, restart_timeout
'''
63.33 seconds
'''


@pytest.mark.interface
def test_dialog_line(clickOn, node, screenDiffChecker):
    clickOn('play')
    clickOn('radius_modal_yes')
    time.sleep(running_timeout)
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('тестовое правило с лопатой')
    node.asrPub(asr_msg)
    screenDiffChecker('dialog_line.png') is None


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
