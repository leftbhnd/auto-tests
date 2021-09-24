#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
X seconds
'''


@pytest.mark.interaction_print
def test_start_interaction(node):
    node.interactionPub(True, 0)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_print
def test_run_photo_app(click, node):
    node.cancelSpeechPub()
    node.asrPub('сделай фото')
    click(btn.gui.take_photo)
    time.sleep(modals)
    click(btn.gui.print_photo)


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
    click(btn.control.promo)
    click(btn.promo.selector)
    click(btn.promo.printshow)
    click(btn.promo.robot_checkbox1)
    click(btn.promo.remove)
    click(modal.promo.yes)
    assert screenDiffChecker(
        'interaction/deleted_pictures.png'
    ) is None


@pytest.mark.interaction_print
def test_restore(click):
    click(btn.handler.back)
    click(modal.save.yes)
    click(btn.handler.back)
    time.sleep(modals)
