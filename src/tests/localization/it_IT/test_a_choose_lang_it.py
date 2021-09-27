#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
17.77 seconds
'''


@pytest.mark.localization_it_IT
def test_choose_lang(click, typeText, node):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_he)
    click(btn.control.settings_he)
    click(btn.settings.lang_he)
    for i in range(6):
        click(btn.handler.lang_down_arr_he)
    click(btn.lang.it_IT_he)
    click(btn.lang.set_default_he)
    click(btn.handler.back_he)
    click(modal.save.yes_he)
    time.sleep(modals)
    click(btn.handler.back_he)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'it_IT'
