#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
14.75 seconds
'''


@pytest.mark.localization_el_GR
def test_choose_lang(clickOn, typeText, node):
    node.initNode()
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lang_settings)
    clickOn(btn.lang_el_GR)
    clickOn(btn.lang_set_default)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
    node.killNode()
    assert node.getSystemLanguage() == 'el_GR'
