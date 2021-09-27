#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
17.77 seconds
'''


@pytest.mark.localization_es_ES
def test_choose_lang(click, typeText, node):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.lang)
    for i in range(6):
        click(btn.handler.lang_down_arr)
    click(btn.lang.es_ES)
    click(btn.lang.set_default)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'es_ES'
