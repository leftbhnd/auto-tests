#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly, modals, running, restart, btn, modal
from src.helpers.messages import AsrTtsMsg
'''
145.81 seconds
'''


@pytest.mark.localization_sv_SE
def test_no_connection_modal(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.answers_log)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(35)
    clickOn(btn.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/sv_SE/no_connection_modal.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_radius_modal(clickOn, screenDiffChecker):
    clickOn(modal.no_connection_yes)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/sv_SE/radius_modal.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn(modal.radius_yes)
    assert screenDiffChecker(
        'localization/sv_SE/run_state.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/sv_SE/run_active.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/sv_SE/run.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_answer_log(clickOn, node, screenDiffChecker):
    time.sleep(running)
    clickOn(modal.ans_log_clear)
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('spade testregel')
    node.asrPub(asr_msg)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/sv_SE/test_answers_log.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_sv_SE
def test_speech_settings(clickOn, screenDiffChecker):
    clickOn(modal.ans_log_close)
    clickOn(btn.speech_settings)
    assert screenDiffChecker(
        'localization/sv_SE/speech_settings.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_sv_SE
def test_testing_script(openPasswordModal, clickOn, typeText, screenDiffChecker):
    clickOn(modal.speech_settings_close)
    openPasswordModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.testing)
    time.sleep(modals)
    clickOn(btn.test_hand_right)
    assert screenDiffChecker(
        'localization/sv_SE/script_is_running.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_main_camera(clickOn, screenDiffChecker):
    time.sleep(8)
    clickOn(btn.test_main_camera)
    assert screenDiffChecker(
        'localization/sv_SE/testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_sv_SE
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.test_videostream_close)
    clickOn(btn.test_fr)
    assert screenDiffChecker(
        'localization/sv_SE/testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_sv_SE
def test_bottom_camera(clickOn, screenDiffChecker):
    clickOn(btn.test_videostream_close)
    clickOn(btn.test_bottom)
    assert screenDiffChecker(
        'localization/sv_SE/testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_sv_SE
def test_fisheye_camera(clickOn, screenDiffChecker):
    clickOn(btn.test_videostream_close)
    clickOn(btn.test_fisheye)
    assert screenDiffChecker(
        'localization/sv_SE/testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_sv_SE
def test_periphery_statuses(clickOn, screenDiffChecker):
    clickOn(btn.test_videostream_close)
    clickOn(btn.test_periphery_statuses_sv)
    assert screenDiffChecker(
        'localization/sv_SE/periphery_statuses_modal.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_record_sound_start(clickOn, screenDiffChecker):
    clickOn(btn.test_periphery_statuses_close)
    clickOn(btn.test_record_sound)
    assert screenDiffChecker(
        'localization/sv_SE/testing_record_sound_start.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_record_sound_finish(clickOn, screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker(
        'localization/sv_SE/testing_record_sound_finish.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_auto_mode_popup(clickOn, typeText, screenDiffChecker):
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.auto_mode)
    clickOn(btn.back)
    assert screenDiffChecker(
        'localization/sv_SE/automode_popup.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_joy_mode_popup(clickOn, typeText, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.auto_mode)
    clickOn(btn.back)
    assert screenDiffChecker(
        'localization/sv_SE/joy_mode_popup.png'
    ) is None


@pytest.mark.localization_sv_SE
def test_restore():
    time.sleep(modals)
