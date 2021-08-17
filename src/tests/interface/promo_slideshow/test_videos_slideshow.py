#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
18.72 seconds
'''


@pytest.mark.slideshow_videos
def test_promo_open(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('promo')
    assert screenDiffChecker('promo.png') is None


@pytest.mark.slideshow_videos
def test_add_video(clickOn, screenDiffChecker):
    clickOn('promo_videos')
    clickOn('promo_videos')
    clickOn('fs_promo_checkbox1')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('add_video_slideshow.png') is None


@pytest.mark.slideshow_videos
def test_add_two_videos(clickOn, screenDiffChecker):
    clickOn('fs_promo_checkbox2')
    clickOn('fs_promo_checkbox3')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('add_three_videos_slideshow.png') is None


@pytest.mark.slideshow_videos
def test_add_all_videos(clickOn, screenDiffChecker):
    clickOn('fs_promo_choose_all')
    clickOn('promo_add')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('add_all_videos_slideshow.png') is None


@pytest.mark.slideshow_videos
def test_delete_video(clickOn, screenDiffChecker):
    clickOn('robot_promo_checkbox1')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('delete_video_slideshow.png') is None


@pytest.mark.slideshow_videos
def test_delete_two_videos(clickOn, screenDiffChecker):
    clickOn('robot_promo_checkbox2')
    clickOn('robot_promo_checkbox3')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('delete_two_videos_slideshow.png') is None


@pytest.mark.slideshow_videos
def test_delete_all_videos(clickOn, screenDiffChecker):
    clickOn('robot_promo_choose_all')
    clickOn('promo_delete')
    clickOn('promo_modal_yes')
    assert screenDiffChecker('delete_all_videos_slideshow.png') is None

@pytest.mark.slideshow_videos
def test_reset(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('save_modal_yes')
    clickOn('back')
