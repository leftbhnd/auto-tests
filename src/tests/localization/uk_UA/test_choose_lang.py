#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
20.76 seconds
'''


@pytest.mark.localization_uk_UA
def test_choose_lang(clickOn, typeText, node):
    node.initNode()
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lang_settings)
    for i in range(12):
        clickOn(btn.lang_down_arrow)
    clickOn(btn.lang_uk_UA)
    clickOn(btn.lang_set_default)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
    node.killNode()
    assert node.getSystemLanguage() == 'uk_UA'
