#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from src.helpers.config import btn, modal
'''
8.60 seconds
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
    click(btn.handler.reset)
    click(btn.handler.back)
    click(btn.handler.back_ae)
    click(btn.handler.back_ae)
    click(btn.handler.reset)
    assert node.getSystemLanguage() == 'ar_AE'
