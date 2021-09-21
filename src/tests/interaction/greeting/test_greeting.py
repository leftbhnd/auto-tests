#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, params
'''
TODO добполнить тест
X seconds
'''


# @pytest.mark.interaction_greeting
# def test_set_greeting_timeout(clickOn, openServiceMenu):
#     openServiceMenu()
#     clickOn(btn.settings)
#     clickOn(btn.system)
#     clickOn(btn.system_dialog)
#     clickOn(btn.system_dialog_down_arrow)
#     for i in range(5):
#         clickOn(params.timeRecently_decrease)
#     for i in range(2):
#         clickOn(params.timeRecentlyUnknown_decrease)
#     clickOn(btn.back)
#     clickOn(modal.save_yes)
#     time.sleep(modals)
#     clickOn(btn.back)
#     clickOn(btn.back)
#     time.sleep(modals)


@pytest.mark.interaction_greeting
def test_greeting_unknown(node):
    node.facePub(3, True, 0, 0, 3, 1.0)
    assert node.getTts() == 'тестовый привет, незнакомец'


@pytest.mark.interaction_greeting
def test_greeting_known(node):
    node.clearFacePub()
    node.facePub(2, True, 1, 1632114331, 2, 0.9)
    assert node.getTts() == 'тестовый привет, ДМИТРИЙЙ'


# @pytest.mark.interaction_greeting
# def test_restore(clickOn, openServiceMenu, node):
#     node.clearFacePub()
#     openServiceMenu()
#     clickOn(btn.settings)
#     clickOn(btn.system)
#     clickOn(btn.system_dialog)
#     clickOn(btn.system_dialog_down_arrow)
#     for i in range(5):
#         clickOn(params.timeRecently_increase)
#     for i in range(2):
#         clickOn(params.timeRecentlyUnknown_increase)
#     clickOn(btn.back)
#     clickOn(modal.save_yes)
#     time.sleep(modals)
#     clickOn(btn.back)
#     clickOn(btn.back)
#     time.sleep(modals)
