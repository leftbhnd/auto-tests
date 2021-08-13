#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
54.65 seconds
'''


@pytest.mark.slideshow_pictures
def test_promo_open(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('promo')
    assert screenDiffChecker('promo.png') is None


@pytest.mark.slideshow_pictures
def test_promo_add_picture(clickOn, screenDiffChecker):
    clickOn('promo_pictures')
    clickOn('promo_pictures')
    clickOn('fs_promo_checkbox1')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('promo_picture_slideshow.png') is None


@pytest.mark.slideshow_pictures
def test_promo_add_two_pictures(clickOn, screenDiffChecker):
    clickOn('fs_promo_checkbox2')
    clickOn('fs_promo_checkbox3')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('promo_three_pictures_slideshow.png') is None


@pytest.mark.slideshow_pictures
def test_promo_add_all_pictures(clickOn, screenDiffChecker):
    clickOn('fs_promo_choose_all')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('promo_all_pictures_slideshow.png') is None


@pytest.mark.slideshow_pictures
def test_reset(clickOn, screenDiffChecker):
    clickOn('robot_promo_checkbox1')
    clickOn('robot_promo_choose_all')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    clickOn('back')
    clickOn('save_modal_yes')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert screenDiffChecker('startHZ.png') is None
