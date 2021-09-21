#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, params
from src.helpers.messages import FaceMsg
'''
TODO добполнить тест
X seconds
'''


@pytest.mark.interaction_greeting
def test_greeting_unknown(node):
    face_msg = FaceMsg(2, False, 22, 212, 0.9)
    node.facePub(face_msg)
    time.sleep(5)
    assert node.getTts() == 'тестовый привет, незнакомец'


@pytest.mark.interaction_greeting
def test_greeting_known(node):
    face_msg = FaceMsg(3, False, 23, 1632114331, 0.9)
    node.facePub(face_msg)
    time.sleep(5)
    assert node.getTts() == 'тестовый привет, ДМИТРИЙЙ'


@pytest.mark.interaction_greeting
def test_restore(clickOn, openServiceMenu):
    openServiceMenu()
    clickOn(btn.settings)
    clickOn(btn.system)
    clickOn(btn.system_dialog)
    clickOn(btn.system_dialog_down_arrow)
    for i in range(5):
        clickOn(params.timeRecently_increase)
    for i in range(2):
        clickOn(params.timeRecentlyUnknown_increase)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
