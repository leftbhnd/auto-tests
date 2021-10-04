#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
17.59 seconds
'''


@pytest.mark.localization_zh_CN
def test_choose_lang(click, typeText, node):
    click(btn.start.control)
    typeText(123456)
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.lang)
    for i in range(13):
        click(btn.handler.lang_down_arr)
    click(btn.lang.zn_CN)
    click(btn.lang.set_default)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.reset)
    assert node.getSystemLanguage() == 'zh_CN'
