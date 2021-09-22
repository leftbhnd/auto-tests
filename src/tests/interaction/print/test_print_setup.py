#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
X seconds
'''


@pytest.mark.interaction_print_setup
def test_add_promo(clickOn, openServiceMenu, screenDiffChecker):
    openServiceMenu()
    clickOn(btn.promo)
    clickOn(btn.promo_selector)
    clickOn(btn.promo_print)
    clickOn(btn.promo_pictures)
    clickOn(btn.promo_pictures)
    clickOn(btn.promo_fs_checkbox1)
    clickOn(btn.promo_add)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interaction/added_picture.png'
    ) is None


@pytest.mark.interaction_print_setup
def test_restore(clickOn):
    clickOn(btn.back)
    clickOn(modal.save_yes)
    clickOn(btn.back)
    time.sleep(modals)
