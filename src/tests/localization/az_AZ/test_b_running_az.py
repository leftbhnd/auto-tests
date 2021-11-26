#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, slowly, modals, running, restart
'''
132.53 seconds
'''


@pytest.mark.localization_az_AZ
def test_no_connection_modal(click, typeText, screenDiffChecker):
    click(btn.start.control)
    typeText(123456)
    click(modal.pwd.ok)
    click(btn.control.answers_log)
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(20)
    click(btn.start.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/az_AZ/run_no_connection_modal.png',
        (370, 310, 540, 180)
    ) is None


@pytest.mark.localization_az_AZ
def test_radius_modal(click, screenDiffChecker):
    click(modal.no_connection.yes)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/az_AZ/run_radius_modal.png',
        (370, 300, 540, 190)
    ) is None


@pytest.mark.localization_az_AZ
def test_check_run_state(click, screenDiffChecker):
    click(modal.radius.yes)
    assert screenDiffChecker(
        'localization/az_AZ/run_state.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/az_AZ/run_active.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_check_run(screenDiffChecker):
    time.sleep(0.7)
    assert screenDiffChecker(
        'localization/az_AZ/run.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_answer_log(click, screenDiffChecker, node):
    time.sleep(running)
    node.cancelSpeechPub()
    click(modal.ans_log.clear_ae)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/az_AZ/run_test_answers_log.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_az_AZ
def test_speech_settings(click, screenDiffChecker):
    click(modal.ans_log.close)
    click(btn.gui.speech_settings)
    assert screenDiffChecker(
        'localization/az_AZ/run_speech_settings.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_az_AZ
def test_testing_script(click, openServiceMenu, screenDiffChecker, node):
    node.cancelSpeechPub()
    node.cancelScriptPub()
    click(modal.speech_settings.close)
    openServiceMenu()
    click(btn.control.testing)
    time.sleep(modals)
    click(btn.testing.hand_right)
    assert screenDiffChecker(
        'localization/az_AZ/run_script_is_running.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_main_camera(click, screenDiffChecker, node):
    node.cancelScriptPub()
    click(btn.handler.reset)
    click(btn.testing.main_camera)
    assert screenDiffChecker(
        'localization/az_AZ/run_testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_az_AZ
def test_face_recognize(click, screenDiffChecker):
    click(modal.testing.videostream_close)
    click(btn.testing.fr)
    assert screenDiffChecker(
        'localization/az_AZ/run_testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_az_AZ
def test_bottom_camera(click, screenDiffChecker):
    click(modal.testing.videostream_close)
    click(btn.testing.bottom)
    assert screenDiffChecker(
        'localization/az_AZ/run_testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_az_AZ
def test_fisheye_camera(click, screenDiffChecker):
    click(modal.testing.videostream_close)
    click(btn.testing.fisheye)
    assert screenDiffChecker(
        'localization/az_AZ/run_testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_az_AZ
def test_periphery_statuses(click, screenDiffChecker):
    click(modal.testing.videostream_close)
    click(btn.testing.periphery_statuses)
    assert screenDiffChecker(
        'localization/az_AZ/run_periphery_statuses_modal.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_record_sound_start(click, screenDiffChecker):
    click(modal.testing.periphery_close)
    click(btn.testing.record)
    assert screenDiffChecker(
        'localization/az_AZ/run_testing_record_sound_start.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_record_sound_finish(screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker(
        'localization/az_AZ/run_testing_record_sound_finish.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_restore(click):
    click(btn.handler.back)
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
