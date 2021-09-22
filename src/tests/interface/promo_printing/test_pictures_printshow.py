#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time


from src.helpers.config import modals, btn, modal
'''
22.41 seconds
'''


@pytest.mark.interface_promo_printing
def test_promo_open(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.promo)
    assert screenDiffChecker(
        'interfaces/promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.interface_promo_printing
def test_add_picture(click, screenDiffChecker):
    click(btn.promo_selector)
    click(btn.promo_print)
    click(btn.promo_pictures)
    click(btn.promo_pictures)
    click(btn.promo_fs_checkbox1)
    click(btn.promo_add)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/add_picture_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_add_two_pictures(click, screenDiffChecker):
    click(btn.promo_fs_checkbox2)
    click(btn.promo_fs_checkbox3)
    click(btn.promo_add)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/add_three_pictures_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_add_all_pictures(click, screenDiffChecker):
    click(btn.promo_fs_choose_all)
    click(btn.promo_add)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/add_all_pictures_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_picture(click, screenDiffChecker):
    click(btn.promo_robot_checkbox1)
    click(btn.promo_delete)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/delete_picture_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_two_pictures(click, screenDiffChecker):
    click(btn.promo_robot_checkbox2)
    click(btn.promo_robot_checkbox3)
    click(btn.promo_delete)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/delete_two_pictures_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_all_pictures(click, screenDiffChecker):
    click(btn.promo_robot_choose_all)
    click(btn.promo_delete)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/delete_all_pictures_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_reset(click):
    click(btn.back)
    click(modal.save_yes)
    click(btn.back)
    time.sleep(modals)
