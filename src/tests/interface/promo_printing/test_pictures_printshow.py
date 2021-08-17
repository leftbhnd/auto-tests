#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
19.73 seconds
'''


@pytest.mark.printshow_pictures
def test_promo_open(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('promo')
    assert screenDiffChecker('promo.png') is None


@pytest.mark.printshow_pictures
def test_add_picture(clickOn, screenDiffChecker):
    clickOn('promo_selector')
    clickOn('promo_choose_print')
    clickOn('promo_pictures')
    clickOn('promo_pictures')
    clickOn('fs_promo_checkbox1')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('add_picture_printshow.png') is None


@pytest.mark.printshow_pictures
def test_add_two_pictures(clickOn, screenDiffChecker):
    clickOn('fs_promo_checkbox2')
    clickOn('fs_promo_checkbox3')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('add_three_pictures_printshow.png') is None


@pytest.mark.printshow_pictures
def test_add_all_pictures(clickOn, screenDiffChecker):
    clickOn('fs_promo_choose_all')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('add_all_pictures_printshow.png') is None


@pytest.mark.printshow_pictures
def test_delete_picture(clickOn, screenDiffChecker):
    clickOn('robot_promo_checkbox1')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('delete_picture_printshow.png') is None


@pytest.mark.printshow_pictures
def test_delete_two_pictures(clickOn, screenDiffChecker):
    clickOn('robot_promo_checkbox2')
    clickOn('robot_promo_checkbox3')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('delete_two_pictures_printshow.png') is None


@pytest.mark.printshow_pictures
def test_delete_all_pictures(clickOn, screenDiffChecker):
    clickOn('robot_promo_choose_all')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('delete_all_pictures_printshow.png') is None


@pytest.mark.printshow_pictures
def test_reset(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('save_modal_yes')
    clickOn('back')