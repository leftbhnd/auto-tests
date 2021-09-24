#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
17.75 seconds
'''


@pytest.mark.localization_he_IL
def test_choose_lang(click, type, node):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    type('123456')
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.lang)
    for i in range(6):
        click(btn.lang.down_arrow)
    click(btn.lang.he_IL)
    click(btn.lang.set_default)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back_he)
    click(btn.handler.back_he)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'he_IL'
