#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
X seconds
'''


@pytest.mark.interaction_promo_setup
def test_add_promo(clickOn, typeText, openPwdModal, screenDiffChecker):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.promo)
    clickOn(btn.promo_pictures)
    clickOn(btn.promo_pictures)
    clickOn(btn.promo_fs_checkbox1)
    clickOn(btn.promo_fs_checkbox2)
    clickOn(btn.promo_add)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interaction/promo_pictures.png'
    ) is None


@pytest.mark.interaction_promo_setup
def test_restore(clickOn):
    clickOn(btn.back)
    clickOn(modal.save_yes)
    clickOn(btn.back)
    time.sleep(modals)
