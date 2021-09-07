#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly, modals, running, restart, btn, modal
from src.helpers.messages import AsrTtsMsg
'''
X seconds
'''


@pytest.mark.localization_ar_AE
def test_no_connection_modal(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.inv_answers_log)
    clickOn(btn.inv_restart)
    clickOn(modal.inv_restart_yes)
    time.sleep(30)
    clickOn(btn.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/no_connection_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_radius_modal(clickOn, screenDiffChecker):
    clickOn(modal.inv_no_connection_yes)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/radius_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_check_run_state(clickOn, screenDiffChecker):
    clickOn(modal.inv_radius_yes)
    assert screenDiffChecker(
        'localization/ar_AE/run_state.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/ar_AE/run_active.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/ar_AE/run.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_answer_log(clickOn, node, screenDiffChecker):
    node.initNode()
    time.sleep(running)
    clickOn(modal.inv_ans_log_clear)
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('חוק בדיקת אתים')
    node.asrPub(asr_msg)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/test_answers_log.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_ar_AE
def test_speech_settings(clickOn, screenDiffChecker):
    clickOn(modal.inv_ans_log_close)
    clickOn(btn.inv_speech_settings)
    assert screenDiffChecker(
        'localization/ar_AE/speech_settings.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_ar_AE
def test_testing_script(openPasswordModal, clickOn, typeText, screenDiffChecker):
    clickOn(modal.inv_speech_settings_close)
    openPasswordModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.inv_testing)
    time.sleep(modals)
    clickOn(btn.inv_test_hand_right)
    assert screenDiffChecker(
        'localization/ar_AE/script_is_running.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_main_camera(clickOn, screenDiffChecker):
    time.sleep(8)
    clickOn(btn.inv_test_main_camera)
    assert screenDiffChecker(
        'localization/ar_AE/testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ar_AE
def test_face_recognize(clickOn, screenDiffChecker):
    clickOn(btn.inv_test_videostream_close)
    clickOn(btn.inv_test_fr)
    assert screenDiffChecker(
        'localization/ar_AE/testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ar_AE
def test_bottom_camera(clickOn, screenDiffChecker):
    clickOn(btn.inv_test_videostream_close)
    clickOn(btn.inv_test_bottom)
    assert screenDiffChecker(
        'localization/ar_AE/testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ar_AE
def test_fisheye_camera(clickOn, screenDiffChecker):
    clickOn(btn.inv_test_videostream_close)
    clickOn(btn.inv_test_fisheye)
    assert screenDiffChecker(
        'localization/ar_AE/testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ar_AE
def test_periphery_statuses(clickOn, screenDiffChecker):
    clickOn(btn.inv_test_videostream_close)
    clickOn(btn.inv_test_periphery_statuses)
    assert screenDiffChecker(
        'localization/ar_AE/periphery_statuses_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_record_sound_start(clickOn, screenDiffChecker):
    clickOn(btn.inv_test_periphery_statuses_close)
    clickOn(btn.inv_test_record_sound)
    assert screenDiffChecker(
        'localization/ar_AE/testing_record_sound_start.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_record_sound_finish(clickOn, screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker(
        'localization/ar_AE/testing_record_sound_finish.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_auto_mode_popup(clickOn, typeText, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(btn.inv_restart)
    clickOn(modal.inv_restart_yes)
    time.sleep(restart)
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.inv_auto_mode)
    clickOn(btn.inv_back)
    assert screenDiffChecker(
        'localization/ar_AE/automode_popup.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_joy_mode_popup(clickOn, typeText, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.inv_auto_mode)
    clickOn(btn.inv_back)
    assert screenDiffChecker(
        'localization/ar_AE/joy_mode_popup.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_restore(node):
    node.killNode()
    time.sleep(modals)
