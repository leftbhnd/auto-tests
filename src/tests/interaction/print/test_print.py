#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
X seconds
'''


@pytest.mark.interaction_print
def test_start_interaction(click, node):
    node.interactionPub(True, 0)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_print
def test_run_photo_app(click, node):
    node.cancelSpeechPub()
    node.asrPub('сделай фото')
    click(btn.take_photo)
    time.sleep(modals)
    click(btn.print_photo)


@pytest.mark.interaction_print
def test_check_printshow(screenDiffChecker):
    assert screenDiffChecker(
        'interaction/print.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interaction_print
def test_delete_pictures(click, openServiceMenu, screenDiffChecker):
    # TODO посчитать таймаут
    time.sleep(30)
    openServiceMenu()
    click(btn.promo)
    click(btn.promo_selector)
    click(btn.promo_print)
    click(btn.promo_robot_checkbox1)
    click(btn.promo_delete)
    click(modal.promo_yes)
    assert screenDiffChecker(
        'interaction/deleted_pictures.png'
    ) is None


@pytest.mark.interaction_print
def test_restore(click):
    click(btn.back)
    click(modal.save_yes)
    click(btn.back)
    time.sleep(modals)
