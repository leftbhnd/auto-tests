#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.testConfig import modals_timeout
'''
22.44 seconds
'''


@pytest.mark.interface_promo_printing
def test_promo_open(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('promo')
    assert screenDiffChecker(
        'interfaces/promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.interface_promo_printing
def test_add_video(clickOn, screenDiffChecker):
    clickOn('promo_selector')
    clickOn('promo_choose_print')
    clickOn('promo_videos')
    clickOn('promo_videos')
    clickOn('fs_promo_checkbox1')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker(
        'interfaces/add_video_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_add_two_videos(clickOn, screenDiffChecker):
    clickOn('fs_promo_checkbox2')
    clickOn('fs_promo_checkbox3')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker(
        'interfaces/add_three_videos_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_add_all_videos(clickOn, screenDiffChecker):
    clickOn('fs_promo_choose_all')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker(
        'interfaces/add_all_videos_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_video(clickOn, screenDiffChecker):
    clickOn('robot_promo_checkbox1')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    assert screenDiffChecker(
        'interfaces/delete_video_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_two_videos(clickOn, screenDiffChecker):
    clickOn('robot_promo_checkbox2')
    clickOn('robot_promo_checkbox3')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    assert screenDiffChecker(
        'interfaces/delete_two_videos_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_all_videos(clickOn, screenDiffChecker):
    clickOn('robot_promo_choose_all')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    assert screenDiffChecker(
        'interfaces/delete_all_videos_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_reset(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('save_modal_yes')
    clickOn('back')
    time.sleep(modals_timeout)
