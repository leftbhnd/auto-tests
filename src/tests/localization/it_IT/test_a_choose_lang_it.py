#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
17.77 seconds
'''


@pytest.mark.localization_it_IT
def test_choose_lang(click, type, node):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    type('123456')
    click(modal.pwd.ok_he)
    click(btn.inv_settings)
    click(btn.inv_lang_settings)
    for i in range(6):
        click(btn.inv_lang_down_arrow)
    click(btn.inv_lang_it_IT)
    click(btn.inv_lang_set_default)
    click(btn.handler.back_he)
    click(modal.inv_save_yes)
    time.sleep(modals)
    click(btn.handler.back_he)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'it_IT'
