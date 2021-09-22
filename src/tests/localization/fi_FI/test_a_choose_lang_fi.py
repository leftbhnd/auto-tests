#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
17.77 seconds
'''


@pytest.mark.localization_fi_FI
def test_choose_lang(click, type, node):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.settings)
    click(btn.lang_settings)
    for i in range(6):
        click(btn.lang_down_arrow)
    click(btn.lang_fi_FI)
    click(btn.lang_set_default)
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.back)
    click(btn.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'fi_FI'
