#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
20.76 seconds
'''


@pytest.mark.localization_ru_RU
def test_choose_lang(click, type, node):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    type('123456')
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.lang)
    for i in range(12):
        click(btn.lang.down_arr)
    click(btn.lang.ru_RU)
    click(btn.lang.set_default)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'ru_RU'
