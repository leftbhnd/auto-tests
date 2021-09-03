#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
X seconds
'''


@pytest.mark.localization_fr_FR
def test_choose_lang(clickOn, typeText, node):
    node.initNode()
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lang_settings)
    for i in range(6):
        clickOn(btn.lang_down_arrow)
    clickOn(btn.lang_fr_FR)
    clickOn(btn.lang_set_default)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
    node.killNode()
    assert node.getSystemLanguage() == 'fr_FR'