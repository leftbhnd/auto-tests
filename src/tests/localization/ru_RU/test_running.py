#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.testConfig import modals_timeout, running_timeout, restart_timeout
from src.helpers.messages import AsrTtsMsg
'''
X seconds
'''


@pytest.mark.localization_ru_RU
def test_no_connection_modal(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('answers_log')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(30)
    clickOn('play')
    time.sleep(slower_timeout)
    assert screenDiffChecker(
        'localization/ru_RU/ru_no_connection_modal.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_radius_modal(clickOn, screenDiffChecker):
    clickOn('no_connection_modal_yes')
    time.sleep(slower_timeout)
    assert screenDiffChecker(
        'localization/ru_RU/ru_radius_modal.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn('radius_modal_yes')
    assert screenDiffChecker(
        'localization/ru_RU/ru_run_state.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/ru_RU/ru_run_active.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/ru_RU/ru_run.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_answer_log(node, screenDiffChecker):
    time.sleep(running_timeout)
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('тестовое правило с лопатой')
    node.asrPub(asr_msg)
    screenDiffChecker(
        'localization/ru_RU/ru_test_answers_log.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_ru_RU
def test_speech_settings(clickOn, screenDiffChecker):
    clickOn('answers_log_modal_close')
    clickOn('speech_settings')
    screenDiffChecker(
        'localization/ru_RU/ru_speech_settings.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_ru_RU
def test_testing_script(openPasswordModal, clickOn, typeText, screenDiffChecker):
    openPasswordModal()
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('testing')
    clickOn('test_hand_right')
    screenDiffChecker(
        'localization/ru_RU/ru_script_is_running.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_testing_script(openPasswordModal, clickOn, typeText, screenDiffChecker):
    openPasswordModal()
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('testing')
    clickOn('test_hand_right')
    screenDiffChecker(
        'localization/ru_RU/ru_script_is_running.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_main_camera(clickOn, screenDiffChecker):
    time.sleep(8)
    clickOn('testing_main_camera')
    assert screenDiffChecker(
        'localization/ru_RU/ru_testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ru_RU
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn('testing_videostream_close')
    clickOn('testing_face_recognize')
    assert screenDiffChecker(
        'localization/ru_RU/ru_testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ru_RU
def test_bottom_camera(clickOn, screenDiffChecker):
    clickOn('testing_videostream_close')
    clickOn('testing_bottom_camera')
    assert screenDiffChecker(
        'localization/ru_RU/ru_testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ru_RU
def test_fisheye_camera(clickOn, screenDiffChecker):
    clickOn('testing_videostream_close')
    clickOn('testing_fisheye_camera')
    assert screenDiffChecker(
        'localization/ru_RU/ru_testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ru_RU
def test_periphery_statuses(clickOn, screenDiffChecker):
    clickOn('testing_videostream_close')
    clickOn('periphery_statuses')
    assert screenDiffChecker(
        'localization/ru_RU/ru_periphery_statuses_modal.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_record_sound_start(clickOn, screenDiffChecker):
    clickOn('periphery_statuses_close')
    clickOn('testing_record_sound')
    assert screenDiffChecker(
        'localization/ru_RU/ru_testing_record_sound_start.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_record_sound_finish(clickOn, screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker(
        'localization/ru_RU/ru_testing_record_sound_finish.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_auto_mode_popup(clickOn, typeText, screenDiffChecker):
    clickOn('back')
    clickOn('answers_log')
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(restart_timeout)
    clickOn('control')
    typeText('123456')
    clickOn('pass_modal_yes')
    clickOn('auto_mode')
    clickOn('back')
    screenDiffChecker(
        'localization/ru_RU/ru_automode_popup.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_joy_mode_popup(clickOn, typeText, screenDiffChecker):
    time.sleep(modals_timeout)
    clickOn('control')
    typeText('123456')
    clickOn('pass_modal_yes')
    clickOn('auto_mode')
    clickOn('back')
    screenDiffChecker(
        'localization/ru_RU/ru_joy_mode_popup.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_restore():
    time.sleep(modals_timeout)
