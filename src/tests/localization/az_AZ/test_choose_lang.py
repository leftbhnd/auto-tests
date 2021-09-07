#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
X seconds
'''


@pytest.mark.localization_az_AZ
def test_choose_lang(clickOn, typeText, node):
    node.initNode()
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.change_lang)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.inv_settings)
    clickOn(btn.inv_lang_settings)
    clickOn(btn.inv_lang_az_AZ)
    clickOn(btn.inv_lang_set_default)
    clickOn(btn.inv_back)
    clickOn(modal.inv_save_yes)
    time.sleep(modals)
    clickOn(btn.inv_back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
    node.killNode()
    assert node.getSystemLanguage() == 'az_AZ'
