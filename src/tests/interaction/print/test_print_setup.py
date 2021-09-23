#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
X seconds
'''


@pytest.mark.interaction_print_setup
def test_add_promo(click, openServiceMenu, screenDiffChecker):
    openServiceMenu()
    click(btn.control.promo)
    click(btn.promo.selector)
    click(btn.promo.printshow)
    click(btn.promo.pictures)
    click(btn.promo.pictures)
    click(btn.promo.fs_checkbox1)
    click(btn.promo.add)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interaction/added_picture.png'
    ) is None


@pytest.mark.interaction_print_setup
def test_restore(click):
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.back)
    time.sleep(modals)
