#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
16.76 seconds
'''


@pytest.mark.localization_cs_CZ
def test_choose_lang(clickOn, typeText, node):
    node.initNode()
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lang_settings)
    clickOn(btn.lang_cz_CZ)
    clickOn(btn.lang_set_default)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.back)
    clickOn(btn.back)
    time.sleep(modals)
    node.killNode()
    assert node.getSystemLanguage() == 'cs_CZ'