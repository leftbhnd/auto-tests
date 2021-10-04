#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
17.14 seconds
'''


@pytest.mark.localization_sv_SE
def test_choose_lang(click, typeText, node):
    click(btn.start.control)
    typeText(123456)
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.lang)
    for i in range(12):
        click(btn.handler.lang_down_arr)
    click(btn.lang.sv_SE)
    click(btn.lang.set_default)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.reset)
    assert node.getSystemLanguage() == 'sv_SE'
