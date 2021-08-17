#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.messages import AsrTtsMsg

'''
168.00 seconds
'''


@pytest.mark.testing
def test_testing_open(clickOn, typeText, openPasswordModal, screenDiffChecker):
    clickOn('play')
    clickOn('radius_modal_yes')
    time.sleep(10)
    openPasswordModal()
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('testing')
    assert screenDiffChecker('testing_runned.png') is None


@pytest.mark.testing
def test_rotate_head(clickOn, node):
    clickOn('test_rotate_head')
    node.scriptProcessListener()
    assert node.getScriptProcess() == ['test_rotate_head', True]


@pytest.mark.testing
def test_hand_left(clickOn, node):
    time.sleep(18)
    clickOn('test_hand_left')
    node.scriptProcessListener()
    assert node.getScriptProcess() == ['test_hand_left', True]


@pytest.mark.testing
def test_hand_right(clickOn, node):
    time.sleep(8)
    clickOn('test_hand_right')
    node.scriptProcessListener()
    assert node.getScriptProcess() == ['test_hand_right', True]


@pytest.mark.testing
def test_zero_all_servos(clickOn, node):
    time.sleep(8)
    clickOn('zero_all_servos')
    node.scriptProcessListener()
    assert node.getScriptProcess() == ['reset', True]


@pytest.mark.testing
def test_main_camera(clickOn, screenDiffChecker):
    time.sleep(45)
    clickOn('testing_main_camera')
    assert screenDiffChecker(
        'testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.testing
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn('testing_videostream_close')
    clickOn('testing_face_recognize')
    assert screenDiffChecker(
        'testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.testing
def test_bottom_camera(clickOn, screenDiffChecker):
    clickOn('testing_videostream_close')
    clickOn('testing_bottom_camera')
    assert screenDiffChecker(
        'testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.testing
def test_fisheye_camera(clickOn, screenDiffChecker):
    clickOn('testing_videostream_close')
    clickOn('testing_fisheye_camera')
    assert screenDiffChecker(
        'testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.testing
def test_periphery_statuses(clickOn, screenDiffChecker):
    clickOn('testing_videostream_close')
    clickOn('periphery_statuses')
    assert screenDiffChecker('periphery_statuses_modal.png') is None


@pytest.mark.testing
def test_record_sound_start(clickOn, screenDiffChecker):
    clickOn('periphery_statuses_close')
    clickOn('testing_record_sound')
    assert screenDiffChecker('testing_record_sound_start.png') is None


@pytest.mark.testing
def test_record_sound_finish(clickOn, screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker('testing_record_sound_finish.png') is None


@pytest.mark.testing
def test_speech_recognize(clickOn, node, screenDiffChecker):
    clickOn('testing_speech_recognize')
    asr_msg = AsrTtsMsg('как дела робот',
                        'a6aadeab-5279-17bf-87d2-44e9efbfe5bd'
                        )
    node.asrPub(asr_msg)
    assert screenDiffChecker('testing_speech_recognize.png') is None


@pytest.mark.testing
def test_reset(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert screenDiffChecker('start.png') is None
