#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, default, slowly, modals, running, restart
'''
144.20 seconds
'''


@pytest.mark.localization_az_AZ
def test_no_connection_modal(click, type, screenDiffChecker):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    type('123456')
    click(modal.pwd.ok)
    click(btn.control.answers_log)
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(35)
    click(btn.start.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/az_AZ/run_no_connection_modal.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_radius_modal(click, screenDiffChecker):
    click(modal.no_connection.yes)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/az_AZ/run_radius_modal.png'
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
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/az_AZ/run.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_answer_log(click, screenDiffChecker, node):
    time.sleep(running)
    click(modal.ans_log.clear)
    node.cancelSpeechPub()
    node.asrPub('kürək test qaydası')
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
def test_testing_script(click, openServiceMenu, screenDiffChecker):
    click(modal.speech_settings.close)
    openServiceMenu()
    click(btn.control.testing)
    time.sleep(modals)
    click(btn.testing.hand_right)
    time.sleep(default)
    assert screenDiffChecker(
        'localization/az_AZ/run_script_is_running.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_main_camera(click, screenDiffChecker):
    time.sleep(8)
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
def test_auto_mode_popup(click, type, screenDiffChecker):
    click(btn.handler.back)
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    type('123456')
    click(modal.pwd.ok)
    click(btn.control.auto_mode)
    click(btn.handler.back)
    assert screenDiffChecker(
        'localization/az_AZ/run_automode_popup.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_joy_mode_popup(click, type, screenDiffChecker):
    time.sleep(modals)
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    type('123456')
    click(modal.pwd.ok)
    click(btn.control.auto_mode)
    click(btn.handler.back)
    assert screenDiffChecker(
        'localization/az_AZ/run_joy_mode_popup.png'
    ) is None


@pytest.mark.localization_az_AZ
def test_restore():
    time.sleep(modals)
