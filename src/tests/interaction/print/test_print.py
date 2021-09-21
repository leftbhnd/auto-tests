#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
from src.helpers.messages import InteractionMsg, AsrTtsMsg
'''
X seconds
'''


@pytest.mark.interaction_print
def test_start_interaction(clickOn, node):
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_print
def test_run_photo_app(clickOn, node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('сделай фото')
    node.asrPub(asr_msg)
    clickOn(btn.take_photo)
    time.sleep(modals)
    clickOn(btn.print_photo)


@pytest.mark.interaction_print
def test_check_printshow(screenDiffChecker):
    assert screenDiffChecker(
        'interaction/print.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.interaction_print
def test_delete_pictures(clickOn, openServiceMenu, screenDiffChecker):
    # TODO посчитать таймаут
    time.sleep(30)
    openServiceMenu()
    clickOn(btn.promo)
    clickOn(btn.promo_selector)
    clickOn(btn.promo_print)
    clickOn(btn.promo_robot_checkbox1)
    clickOn(btn.promo_delete)
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'interaction/deleted_pictures.png'
    ) is None


@pytest.mark.interaction_print
def test_restore(clickOn):
    clickOn(btn.back)
    clickOn(modal.save_yes)
    clickOn(btn.back)
    time.sleep(modals)
