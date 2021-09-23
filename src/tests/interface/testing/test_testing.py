#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import running, restart, modals, btn, modal
'''
163.8 seconds
'''


@pytest.mark.interface_testing
def test_testing_open(click, openServiceMenu, screenDiffChecker):
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    openServiceMenu()
    click(btn.testing)
    time.sleep(modals)
    assert screenDiffChecker(
        'interfaces/testing_runned.png'
    ) is None


@pytest.mark.interface_testing
def test_rotate_head(click, node):
    click(btn.test_rotate_head)
    assert node.getScriptProcess() == [True, 'test_rotate_head']


@pytest.mark.interface_testing
def test_hand_left(click, node):
    time.sleep(18)
    click(btn.test_hand_left)
    assert node.getScriptProcess() == [True, 'test_hand_left']


@pytest.mark.interface_testing
def test_hand_right(click, node):
    time.sleep(8)
    click(btn.test_hand_right)
    assert node.getScriptProcess() == [True, 'test_hand_right']


@pytest.mark.interface_testing
def test_zero_all_servos(click, node):
    time.sleep(8)
    click(btn.test_zero_all_servos)
    assert node.getScriptProcess() == [True, 'reset']


@pytest.mark.interface_testing
def test_main_camera(click, screenDiffChecker):
    time.sleep(45)
    click(btn.test_main_camera)
    assert screenDiffChecker(
        'interfaces/testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.interface_testing
def test_face_recognize(click, screenDiffChecker):
    click(btn.test_videostream_close)
    click(btn.test_fr)
    assert screenDiffChecker(
        'interfaces/testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.interface_testing
def test_bottom_camera(click, screenDiffChecker):
    click(btn.test_videostream_close)
    click(btn.test_bottom)
    assert screenDiffChecker(
        'interfaces/testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.interface_testing
def test_fisheye_camera(click, screenDiffChecker):
    click(btn.test_videostream_close)
    click(btn.test_fisheye)
    assert screenDiffChecker(
        'interfaces/testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.interface_testing
def test_periphery_statuses(click, screenDiffChecker):
    click(btn.test_videostream_close)
    click(btn.test_periphery_statuses)
    assert screenDiffChecker(
        'interfaces/periphery_statuses_modal.png'
    ) is None


@pytest.mark.interface_testing
def test_record_sound_start(click, screenDiffChecker):
    click(btn.test_periphery_statuses_close)
    click(btn.test_record_sound)
    assert screenDiffChecker(
        'interfaces/testing_record_sound_start.png'
    ) is None


@pytest.mark.interface_testing
def test_record_sound_finish(screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker(
        'interfaces/testing_record_sound_finish.png'
    ) is None


@pytest.mark.interface_testing
def test_speech_recognize(click, node, screenDiffChecker):
    click(btn.test_speech_recognize)
    node.asrPub('как дела робот')
    assert screenDiffChecker(
        'interfaces/testing_speech_recognize.png'
    ) is None


@pytest.mark.interface_testing
def test_reset(click):
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
