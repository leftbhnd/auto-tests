#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from src.helpers.config import btn, modal
'''
18.08 seconds
'''


@pytest.mark.interface_promo_printing
def test_promo_open(gui):
    gui.click(btn.start.control)
    gui.typeText(123456)
    gui.click(modal.pwd.ok)
    gui.click(btn.control.promo)
    assert screenDiffChecker(
        'interfaces/promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.interface_promo_printing
def test_add_video(gui):
    gui.click(btn.promo.selector)
    gui.click(btn.promo.printshow)
    gui.click(btn.promo.videos)
    gui.click(btn.promo.videos)
    gui.click(btn.promo.fs_checkbox1)
    gui.click(btn.promo.add)
    gui.click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/add_video_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_add_two_videos(gui):
    gui.click(btn.promo.fs_checkbox2)
    gui.click(btn.promo.fs_checkbox3)
    gui.click(btn.promo.add)
    gui.click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/add_three_videos_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_add_all_videos(gui):
    gui.click(btn.promo.fs_choose_all)
    gui.click(btn.promo.add)
    gui.click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/add_all_videos_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_video(gui):
    gui.click(btn.promo.robot_checkbox1)
    gui.click(btn.promo.remove)
    gui.click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/delete_video_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_two_videos(gui):
    gui.click(btn.promo.robot_checkbox2)
    gui.click(btn.promo.robot_checkbox3)
    gui.click(btn.promo.remove)
    gui.click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/delete_two_videos_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_delete_all_videos(click, screenDiffChecker):
    click(btn.promo.robot_choose_all)
    click(btn.promo.remove)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interfaces/delete_all_videos_printshow.png'
    ) is None


@pytest.mark.interface_promo_printing
def test_reset(click):
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.back)
    click(btn.handler.reset)
