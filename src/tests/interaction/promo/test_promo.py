#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal, promo, interaction
'''
X seconds
'''


@pytest.mark.interaction_promo
def test_first_pictures(screenDiffChecker):
    assert screenDiffChecker(
        'interaction/promo1.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interaction_promo
def test_second_picture(screenDiffChecker):
    time.sleep(promo)
    assert screenDiffChecker(
        'interaction/promo2.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interaction_promo
def test_delete_pictures(clickOn, openPwdModal, typeText, screenDiffChecker):
    openPwdModal()
    clickOn(modal.pwd_input)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.promo)
    clickOn(btn.promo_robot_choose_all)
    clickOn(btn.promo_delete)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interaction/deleted_pictures.png'
    ) is None


@pytest.mark.interaction_promo
def test_restore(clickOn):
    clickOn(btn.back)
    clickOn(modal.save_yes)
    clickOn(btn.back)
    time.sleep(interaction)
