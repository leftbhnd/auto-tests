#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
17.77 seconds
'''


@pytest.mark.localization_it_IT
def test_choose_lang(clickOn, typeText, node):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.inv_settings)
    clickOn(btn.inv_lang_settings)
    for i in range(6):
        clickOn(btn.inv_lang_down_arrow)
    clickOn(btn.inv_lang_it_IT)
    clickOn(btn.inv_lang_set_default)
    clickOn(btn.inv_back)
    clickOn(modal.inv_save_yes)
    time.sleep(modals)
    clickOn(btn.inv_back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'it_IT'
