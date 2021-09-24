#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, promo, modals, interaction
'''
44.86 seconds
'''


@pytest.mark.interaction_promo
def test_add_promo(click, openServiceMenu, screenDiffChecker):
    openServiceMenu()
    click(btn.control.promo)
    click(btn.promo.pictures)
    click(btn.promo.pictures)
    click(btn.promo.fs_checkbox1)
    click(btn.promo.fs_checkbox2)
    click(btn.promo.add)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interaction/promo_pictures.png'
    ) is None


@pytest.mark.interaction_promo
def test_first_pictures(click, screenDiffChecker):
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.back)
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
    click(btn.control.promo)
    click(btn.promo.robot_choose_all)
    click(btn.promo.remove)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interaction/deleted_pictures.png'
    ) is None


@pytest.mark.interaction_promo
def test_restore(click):
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.back)
    time.sleep(interaction)
