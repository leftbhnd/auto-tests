#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from src.helpers.config import btn, modal
'''
X seconds
'''


@pytest.mark.load_test
def test_load(click, typeText):
    while True:
        click(btn.start.control)
        click(modal.pwd.input)
        typeText(123456)
        click(modal.pwd.ok)
        click(btn.control.restart)
        click(modal.restart.close)
        click(btn.handler.back)
        click(btn.handler.reset)
