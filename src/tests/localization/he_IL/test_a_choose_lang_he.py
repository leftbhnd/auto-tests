#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
17.75 seconds
'''


@pytest.mark.localization_he_IL
def test_choose_lang(clickOn, typeText, node):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lang_settings)
    for i in range(6):
        clickOn(btn.lang_down_arrow)
    clickOn(btn.lang_he_IL)
    clickOn(btn.lang_set_default)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.inv_back)
    clickOn(btn.inv_back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'he_IL'
