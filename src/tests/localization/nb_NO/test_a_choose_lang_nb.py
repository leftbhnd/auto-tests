#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
14.07 seconds
'''


@pytest.mark.localization_nb_NO
def test_choose_lang(click, typeText, node):
    click(btn.start.control)
    typeText(123456)
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.lang)
    for i in range(6):
        click(btn.handler.lang_down_arr)
    click(btn.lang.nb_NO)
    click(btn.lang.set_default)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.reset)
    assert node.getSystemLanguage() == 'nb_NO'
