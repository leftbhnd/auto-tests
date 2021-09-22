#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import default, slowly, modals, running, restart, btn, modal
'''
146.33 seconds
'''


@pytest.mark.localization_he_IL
def test_no_connection_modal(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.inv_pwd_ok)
    click(btn.inv_answers_log)
    click(btn.inv_restart)
    click(modal.inv_restart_yes)
    time.sleep(35)
    click(btn.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/run_no_connection_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_radius_modal(click, screenDiffChecker):
    click(modal.inv_no_connection_yes)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/run_radius_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_check_run_state(click, screenDiffChecker):
    click(modal.inv_radius_yes)
    assert screenDiffChecker(
        'localization/he_IL/run_state.png'
    ) is None


@pytest.mark.localization_he_IL
def test_check_run_active(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/he_IL/run_active.png'
    ) is None


@pytest.mark.localization_he_IL
def test_check_run(screenDiffChecker):
    time.sleep(0.6)
    assert screenDiffChecker(
        'localization/he_IL/run.png'
    ) is None


@pytest.mark.localization_he_IL
def test_answer_log(click, node, screenDiffChecker):
    time.sleep(running)
    click(modal.inv_ans_log_clear)
    node.cancelSpeechPub()
    node.asrPub('חוק בדיקת אתים')
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/run_test_answers_log.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_he_IL
def test_speech_settings(click, screenDiffChecker):
    click(modal.inv_ans_log_close)
    click(btn.inv_speech_settings)
    assert screenDiffChecker(
        'localization/he_IL/run_speech_settings.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_he_IL
def test_testing_script(openPwdModal, click, type, screenDiffChecker):
    click(modal.inv_speech_settings_close)
    openPwdModal()
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.inv_pwd_ok)
    click(btn.inv_testing)
    time.sleep(modals)
    click(btn.inv_test_hand_right)
    time.sleep(default)
    assert screenDiffChecker(
        'localization/he_IL/run_script_is_running.png'
    ) is None


@pytest.mark.localization_he_IL
def test_main_camera(click, screenDiffChecker):
    time.sleep(8)
    click(btn.inv_test_main_camera)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_he_IL
def test_face_recognize(click, screenDiffChecker):
    click(btn.inv_test_videostream_close)
    click(btn.inv_test_fr)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_he_IL
def test_bottom_camera(click, screenDiffChecker):
    click(btn.inv_test_videostream_close)
    click(btn.inv_test_bottom)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_he_IL
def test_fisheye_camera(click, screenDiffChecker):
    click(btn.inv_test_videostream_close)
    click(btn.inv_test_fisheye)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_he_IL
def test_periphery_statuses(click, screenDiffChecker):
    click(btn.inv_test_videostream_close)
    click(btn.inv_test_periphery_statuses)
    assert screenDiffChecker(
        'localization/he_IL/run_periphery_statuses_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_record_sound_start(click, screenDiffChecker):
    click(btn.inv_test_periphery_statuses_close)
    click(btn.inv_test_record_sound)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_record_sound_start.png'
    ) is None


@pytest.mark.localization_he_IL
def test_record_sound_finish(screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_record_sound_finish.png'
    ) is None


@pytest.mark.localization_he_IL
def test_auto_mode_popup(click, type, screenDiffChecker):
    click(btn.inv_back)
    click(btn.inv_restart)
    click(modal.inv_restart_yes)
    time.sleep(restart)
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.inv_pwd_ok)
    click(btn.inv_auto_mode)
    click(btn.inv_back)
    assert screenDiffChecker(
        'localization/he_IL/run_automode_popup.png'
    ) is None


@pytest.mark.localization_he_IL
def test_joy_mode_popup(click, type, screenDiffChecker):
    time.sleep(modals)
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.inv_pwd_ok)
    click(btn.inv_auto_mode)
    click(btn.inv_back)
    assert screenDiffChecker(
        'localization/he_IL/run_joy_mode_popup.png'
    ) is None


@pytest.mark.localization_he_IL
def test_restore():
    time.sleep(modals)
