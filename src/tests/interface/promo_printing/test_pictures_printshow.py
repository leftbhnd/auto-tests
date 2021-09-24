#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time


from src.helpers.config import btn, modal, modals
'''
22.41 seconds
'''


@pytest.mark.interface_promo_printing
def test_promo_open(click, type, screenDiffChecker):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    type('123456')
    click(modal.pwd.ok)
    click(btn.control.promo)
    assert screenDiffChecker(
        'interfaces/promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.interface_promo_printing
def test_add_picture(click, screenDiffChecker):
    click(btn.promo.selector)
    click(btn.promo.printshow)
    click(btn.promo.pictures)
    click(btn.promo.pictures)
    click(btn.promo.fs_checkbox1)
    click(btn.promo.add)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/add_picture_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_add_two_pictures(click, screenDiffChecker):
    click(btn.promo.fs_checkbox2)
    click(btn.promo.fs_checkbox3)
    click(btn.promo.add)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/add_three_pictures_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_add_all_pictures(click, screenDiffChecker):
    click(btn.promo.fs_choose_all)
    click(btn.promo.add)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/add_all_pictures_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_picture(click, screenDiffChecker):
    click(btn.promo.robot_checkbox1)
    click(btn.promo.remove)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/delete_picture_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_two_pictures(click, screenDiffChecker):
    click(btn.promo.robot_checkbox2)
    click(btn.promo.robot_checkbox3)
    click(btn.promo.remove)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/delete_two_pictures_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_all_pictures(click, screenDiffChecker):
    click(btn.promo.robot_choose_all)
    click(btn.promo.remove)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/delete_all_pictures_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_reset(click):
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.back)
    time.sleep(modals)
