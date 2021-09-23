#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
X seconds
'''


@pytest.mark.interaction_print_setup
def test_add_promo(click, openServiceMenu, screenDiffChecker):
    openServiceMenu()
    click(btn.promo)
    click(btn.promo_selector)
    click(btn.promo_print)
    click(btn.promo_pictures)
    click(btn.promo_pictures)
    click(btn.promo_fs_checkbox1)
    click(btn.promo_add)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interaction/added_picture.png'
    ) is None


@pytest.mark.interaction_print_setup
def test_restore(click):
    click(btn.back)
    click(modal.save_yes)
    click(btn.back)
    time.sleep(modals)
