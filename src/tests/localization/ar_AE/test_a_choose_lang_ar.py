#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
13.58 seconds
'''


@pytest.mark.localization_ar_AE
def test_choose_lang(click, typeText, node):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.lang)
    click(btn.lang.ar_AE)
    click(btn.lang.set_default)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back_ae)
    click(btn.handler.back_ae)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'ar_AE'
