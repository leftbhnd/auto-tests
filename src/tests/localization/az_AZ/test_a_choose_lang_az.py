#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
9.06 seconds
'''


@pytest.mark.localization_az_AZ
def test_choose_lang(click, typeText, node):
    click(btn.start.control)
    click(btn.kb.lang)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_ae)
    click(btn.control.settings_ae)
    click(btn.settings.lang_ae)
    click(btn.lang.az_AZ_ae)
    click(btn.lang.set_default_ae)
    click(btn.handler.back_ae)
    click(modal.save.yes_ae)
    time.sleep(modals)
    click(btn.handler.back_ae)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.reset)
    assert node.getSystemLanguage() == 'az_AZ'
