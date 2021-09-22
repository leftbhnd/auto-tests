#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
17.77 seconds
'''


@pytest.mark.localization_it_IT
def test_choose_lang(click, type, node):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.inv_pwd_ok)
    click(btn.inv_settings)
    click(btn.inv_lang_settings)
    for i in range(6):
        click(btn.inv_lang_down_arrow)
    click(btn.inv_lang_it_IT)
    click(btn.inv_lang_set_default)
    click(btn.inv_back)
    click(modal.inv_save_yes)
    time.sleep(modals)
    click(btn.inv_back)
    click(btn.back)
    click(btn.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'it_IT'
