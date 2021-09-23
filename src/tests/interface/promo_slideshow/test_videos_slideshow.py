#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
21.35 seconds
'''


@pytest.mark.interface_promo_slideshow
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


@pytest.mark.interface_promo_slideshow
def test_add_video(click, screenDiffChecker):
    click(btn.promo_videos)
    click(btn.promo_videos)
    click(btn.promo_fs_checkbox1)
    click(btn.promo_add)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/add_video_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_add_two_videos(click, screenDiffChecker):
    click(btn.promo_fs_checkbox2)
    click(btn.promo_fs_checkbox3)
    click(btn.promo_add)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/add_three_videos_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_add_all_videos(click, screenDiffChecker):
    click(btn.promo_fs_choose_all)
    click(btn.promo_add)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/add_all_videos_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_delete_video(click, screenDiffChecker):
    click(btn.promo_robot_checkbox1)
    click(btn.promo_delete)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/delete_video_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_delete_two_videos(click, screenDiffChecker):
    click(btn.promo_robot_checkbox2)
    click(btn.promo_robot_checkbox3)
    click(btn.promo_delete)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/delete_two_videos_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_delete_all_videos(click, screenDiffChecker):
    click(btn.promo_robot_choose_all)
    click(btn.promo_delete)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interfaces/delete_all_videos_slideshow.png'
    ) is None


@pytest.mark.interface_promo_slideshow
def test_reset(click):
    click(btn.back)
    click(modal.save_yes)
    click(btn.back)
    time.sleep(modals)
