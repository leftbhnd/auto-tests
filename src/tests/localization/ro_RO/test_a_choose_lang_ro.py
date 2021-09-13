#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
21.30 seconds
'''


@pytest.mark.localization_ro_RO
def test_choose_lang(clickOn, typeText, node):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lang_settings)
    for i in range(12):
        clickOn(btn.lang_down_arrow)
    clickOn(btn.lang_ro_RO)
    clickOn(btn.lang_set_default)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'ro_RO'