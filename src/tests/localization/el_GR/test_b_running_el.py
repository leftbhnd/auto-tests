#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, running, restart, btn, modal
'''
146.53 seconds
'''


@pytest.mark.localization_el_GR
def test_no_connection_modal(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.answers_log)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(35)
    click(btn.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/el_GR/run_no_connection_modal.png'
    ) is None


@pytest.mark.localization_el_GR
def test_radius_modal(click, screenDiffChecker):
    click(modal.no_connection_yes)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/el_GR/run_radius_modal.png'
    ) is None


@pytest.mark.localization_el_GR
def test_check_run_state(click, screenDiffChecker):
    click(modal.radius_yes)
    assert screenDiffChecker(
        'localization/el_GR/run_state.png'
    ) is None


@pytest.mark.localization_el_GR
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/el_GR/run_active.png'
    ) is None


@pytest.mark.localization_el_GR
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/el_GR/run.png'
    ) is None


@pytest.mark.localization_el_GR
def test_answer_log(click, node, screenDiffChecker):
    time.sleep(running)
    click(modal.ans_log_clear)
    node.cancelSpeechPub()
    node.asrPub('Κανόνας δοκιμής φτυάρι')
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/el_GR/run_test_answers_log.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_el_GR
def test_speech_settings(click, screenDiffChecker):
    click(modal.ans_log_close)
    click(btn.speech_settings)
    assert screenDiffChecker(
        'localization/el_GR/run_speech_settings.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_el_GR
def test_testing_script(click, openServiceMenu, screenDiffChecker):
    click(modal.speech_settings_close)
    openServiceMenu()
    click(btn.testing)
    time.sleep(modals)
    click(btn.test_hand_right_el)
    time.sleep(default)
    assert screenDiffChecker(
        'localization/el_GR/run_script_is_running.png'
    ) is None


@pytest.mark.localization_el_GR
def test_main_camera(click, screenDiffChecker):
    time.sleep(8)
    click(btn.test_main_camera)
    assert screenDiffChecker(
        'localization/el_GR/run_testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_el_GR
def test_face_recognize(click, screenDiffChecker):
    click(btn.test_videostream_close)
    click(btn.test_fr)
    assert screenDiffChecker(
        'localization/el_GR/run_testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_el_GR
def test_bottom_camera(click, screenDiffChecker):
    click(btn.test_videostream_close)
    click(btn.test_bottom)
    assert screenDiffChecker(
        'localization/el_GR/run_testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_el_GR
def test_fisheye_camera(click, screenDiffChecker):
    click(btn.test_videostream_close)
    click(btn.test_fisheye)
    assert screenDiffChecker(
        'localization/el_GR/run_testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_el_GR
def test_periphery_statuses(click, screenDiffChecker):
    click(btn.test_videostream_close)
    click(btn.test_periphery_statuses)
    assert screenDiffChecker(
        'localization/el_GR/run_periphery_statuses_modal.png'
    ) is None


@pytest.mark.localization_el_GR
def test_record_sound_start(click, screenDiffChecker):
    click(btn.test_periphery_statuses_close)
    click(btn.test_record_sound)
    assert screenDiffChecker(
        'localization/el_GR/run_testing_record_sound_start.png'
    ) is None


@pytest.mark.localization_el_GR
def test_record_sound_finish(screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker(
        'localization/el_GR/run_testing_record_sound_finish.png'
    ) is None


@pytest.mark.localization_el_GR
def test_auto_mode_popup(click, type, screenDiffChecker):
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.auto_mode)
    click(btn.back)
    assert screenDiffChecker(
        'localization/el_GR/run_automode_popup.png'
    ) is None


@pytest.mark.localization_el_GR
def test_joy_mode_popup(click, type, screenDiffChecker):
    time.sleep(modals)
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.auto_mode)
    click(btn.back)
    assert screenDiffChecker(
        'localization/el_GR/run_joy_mode_popup.png'
    ) is None


@pytest.mark.localization_el_GR
def test_restore():
    time.sleep(modals)
