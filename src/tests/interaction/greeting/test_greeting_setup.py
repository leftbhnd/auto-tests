#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal, params
'''
X seconds
'''


@pytest.mark.interaction_greeting_setup
def test_set_greeting_timeout(clickOn, typeText, openPwdModal):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.system)
    clickOn(btn.system_dialog)
    clickOn(btn.system_dialog_down_arrow)
    for i in range(5):
        clickOn(params.timeRecently_decrease)
    for i in range(2):
        clickOn(params.timeRecentlyUnknown_decrease)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
