#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
11.10 seconds
'''


@pytest.mark.localization_en_US
def test_choose_lang(click, typeText, node):
    click(btn.start.control)
    typeText(123456)
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.lang)
    click(btn.lang.en_US)
    click(btn.lang.set_default)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.reset)
    assert node.getSystemLanguage() == 'en_US'
