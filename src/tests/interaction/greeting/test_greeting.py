#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, params
from src.helpers.messages import FaceMsg
'''
TODO добполнить тест
X seconds
'''


@pytest.mark.interaction_greeting
def test_greeting_unknown(node):
    node.initNode()
    face_msg = FaceMsg(2, False, 21, 211, 0.9)
    node.facePub(face_msg)
    assert node.getTts() == 'тестовый привет незнакомец'


@pytest.mark.interaction_greeting
def test_greeting_known(node):
    face_msg = FaceMsg(3, False, 21, X, 0.9)
    node.facePub(face_msg)
    node.killNode()
    assert node.getTts() == 'тестовый привет Дмитрий'


@pytest.mark.interaction_greeting
def test_restore(clickOn, typeText, openPasswordModal):
    openPasswordModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(btn.settings)
    clickOn(btn.system)
    clickOn(btn.system_dialog)
    clickOn(btn.system_dialog_down_arr)
    clickOn(params.timeRecently_increase)
    clickOn(params.timeRecently_increase)
    clickOn(params.timeRecently_increase)
    clickOn(params.timeRecentlyUnknown_increase)
    clickOn(params.timeRecentlyUnknown_increase)
    clickOn(params.timeRecentlyUnknown_increase)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    time.sleep(modals)
