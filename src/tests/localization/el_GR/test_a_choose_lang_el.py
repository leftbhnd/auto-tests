#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
14.75 seconds
'''


@pytest.mark.localization_el_GR
def test_choose_lang(click, typeText, node):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.settings)
    click(btn.settings.lang)
    click(btn.lang.el_GR)
    click(btn.lang.set_default)
    click(btn.handler.back)
    click(modal.save.yes)
    time.sleep(modals)
    click(btn.handler.back)
    click(btn.handler.back)
    click(btn.handler.back)
    time.sleep(modals)
    assert node.getSystemLanguage() == 'el_GR'
