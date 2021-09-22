#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal, promo, interaction
'''
44.86 seconds
'''


@pytest.mark.interaction_promo
def test_add_promo(click, openServiceMenu, screenDiffChecker):
    openServiceMenu()
    click(btn.promo)
    click(btn.promo_pictures)
    click(btn.promo_pictures)
    click(btn.promo_fs_checkbox1)
    click(btn.promo_fs_checkbox2)
    click(btn.promo_add)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interaction/promo_pictures.png'
    ) is None


@pytest.mark.interaction_promo
def test_first_pictures(click, screenDiffChecker):
    click(btn.back)
    click(modal.save_yes)
    click(btn.back)
    time.sleep(modals)
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
def test_delete_pictures(click, openServiceMenu, screenDiffChecker):
    openServiceMenu()
    click(btn.promo)
    click(btn.promo_robot_choose_all)
    click(btn.promo_delete)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interaction/deleted_pictures.png'
    ) is None


@pytest.mark.interaction_promo
def test_restore(click):
    click(btn.back)
    click(modal.save_yes)
    click(btn.back)
    time.sleep(interaction)
