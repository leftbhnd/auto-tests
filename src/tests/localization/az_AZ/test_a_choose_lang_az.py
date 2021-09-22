#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
X seconds
'''


@pytest.mark.localization_az_AZ
def test_choose_lang(click, type, node):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.change_lang)
    click(btn.choose_numbers)
    type('123456')
    click(modal.inv_pwd_ok)
    click(btn.inv_settings)
    click(btn.inv_lang_settings)
    click(btn.inv_lang_az_AZ)
    click(btn.inv_lang_set_default)
    click(btn.inv_back)
    click(modal.inv_save_yes)
    time.sleep(modals)
    click(btn.inv_back)
    click(btn.back)
    click(btn.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'az_AZ'
