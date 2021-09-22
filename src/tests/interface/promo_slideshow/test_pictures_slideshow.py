#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
21.44 seconds
'''


@pytest.mark.interface_promo_slideshow
def test_promo_open(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.promo)
    assert screenDiffChecker(
        'interfaces/promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.interface_promo_slideshow
def test_add_picture(clickOn, screenDiffChecker):
    clickOn(btn.promo_pictures)
    clickOn(btn.promo_pictures)
    clickOn(btn.promo_fs_checkbox1)
    clickOn(btn.promo_add)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/add_picture_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_add_two_pictures(clickOn, screenDiffChecker):
    clickOn(btn.promo_fs_checkbox2)
    clickOn(btn.promo_fs_checkbox3)
    clickOn(btn.promo_add)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/add_three_pictures_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_add_all_pictures(clickOn, screenDiffChecker):
    clickOn(btn.promo_fs_choose_all)
    clickOn(btn.promo_add)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/add_all_pictures_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_delete_picture(clickOn, screenDiffChecker):
    clickOn(btn.promo_robot_checkbox1)
    clickOn(btn.promo_delete)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/delete_picture_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_delete_two_pictures(clickOn, screenDiffChecker):
    clickOn(btn.promo_robot_checkbox2)
    clickOn(btn.promo_robot_checkbox3)
    clickOn(btn.promo_delete)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/delete_two_pictures_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_delete_all_pictures(clickOn, screenDiffChecker):
    clickOn(btn.promo_robot_choose_all)
    clickOn(btn.promo_delete)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/delete_all_pictures_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_reset(clickOn):
    clickOn(btn.back)
    clickOn(modal.save_yes)
    clickOn(btn.back)
    time.sleep(modals)
