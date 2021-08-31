#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.messages import AsrTtsMsg
from src.helpers.config import running, restart, modals, btn, modal
'''
163.8 seconds
'''


@pytest.mark.interface_testing
def test_testing_open(clickOn, typeText, openPasswordModal, screenDiffChecker):
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    openPasswordModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.testing)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/testing_runned.png'
    ) is None


@pytest.mark.interface_testing
def test_rotate_head(clickOn, node):
    node.initNode()
    clickOn(btn.test_rotate_head)
    assert node.getScriptProcess() == ['test_rotate_head', True]


@pytest.mark.interface_testing
def test_hand_left(clickOn, node):
    time.sleep(18)
    clickOn(btn.test_hand_left)
    assert node.getScriptProcess() == ['test_hand_left', True]


@pytest.mark.interface_testing
def test_hand_right(clickOn, node):
    time.sleep(8)
    clickOn(btn.test_hand_right)
    assert node.getScriptProcess() == ['test_hand_right', True]


@pytest.mark.interface_testing
def test_zero_all_servos(clickOn, node):
    time.sleep(8)
    clickOn(btn.test_zero_all_servos)
    assert node.getScriptProcess() == ['reset', True]


@pytest.mark.interface_testing
def test_main_camera(clickOn, screenDiffChecker):
    time.sleep(45)
    clickOn(btn.test_main_camera)
    assert screenDiffChecker(
        'interfaces/testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.interface_testing
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.test_videostream_close)
    clickOn(btn.test_fr)
    assert screenDiffChecker(
        'interfaces/testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.interface_testing
def test_bottom_camera(clickOn, screenDiffChecker):
    clickOn(btn.test_videostream_close)
    clickOn(btn.test_bottom)
    assert screenDiffChecker(
        'interfaces/testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.interface_testing
def test_fisheye_camera(clickOn, screenDiffChecker):
    clickOn(btn.test_videostream_close)
    clickOn(btn.test_fisheye)
    assert screenDiffChecker(
        'interfaces/testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.interface_testing
def test_periphery_statuses(clickOn, screenDiffChecker):
    clickOn(btn.test_videostream_close)
    clickOn(btn.test_periphery_statuses)
    assert screenDiffChecker(
        'interfaces/periphery_statuses_modal.png'
    ) is None


@pytest.mark.interface_testing
def test_record_sound_start(clickOn, screenDiffChecker):
    clickOn(btn.test_periphery_statuses_close)
    clickOn(btn.test_record_sound)
    assert screenDiffChecker(
        'interfaces/testing_record_sound_start.png'
    ) is None


@pytest.mark.interface_testing
def test_record_sound_finish(clickOn, screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker(
        'interfaces/testing_record_sound_finish.png'
    ) is None


@pytest.mark.interface_testing
def test_speech_recognize(clickOn, node, screenDiffChecker):
    clickOn(btn.test_speech_recognize)
    asr_msg = AsrTtsMsg('как дела робот')
    node.asrPub(asr_msg)
    node.killNode()
    assert screenDiffChecker(
        'interfaces/testing_speech_recognize.png'
    ) is None


@pytest.mark.interface_testing
def test_reset(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
