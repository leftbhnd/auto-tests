#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, default, slowly, modals, running, restart
'''
146.33 seconds
'''


@pytest.mark.localization_he_IL
def test_no_connection_modal(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_he)
    click(btn.control.answers_log_he)
    click(btn.control.restart_he)
    click(modal.restart.yes_he)
    time.sleep(35)
    click(btn.start.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/run_no_connection_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_radius_modal(click, screenDiffChecker):
    click(modal.no_connection.yes_he)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/run_radius_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_check_run_state(click, screenDiffChecker):
    click(modal.radius.yes_he)
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
def test_answer_log(click, screenDiffChecker, node):
    time.sleep(running)
    click(modal.ans_log.clear_he)
    node.cancelSpeechPub()
    node.asrPub('חוק בדיקת אתים')
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/run_test_answers_log.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_he_IL
def test_speech_settings(click, screenDiffChecker):
    click(modal.ans_log.close_he)
    click(btn.gui.speech_settings_he)
    assert screenDiffChecker(
        'localization/he_IL/run_speech_settings.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_he_IL
def test_testing_script(click, typeText, openPwdModal, screenDiffChecker):
    click(modal.speech_settings.close_he)
    openPwdModal()
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_he)
    click(btn.control.testing_he)
    time.sleep(modals)
    click(btn.testing.hand_right_he)
    time.sleep(default)
    assert screenDiffChecker(
        'localization/he_IL/run_script_is_running.png'
    ) is None


@pytest.mark.localization_he_IL
def test_main_camera(click, screenDiffChecker):
    time.sleep(8)
    click(btn.testing.main_camera_he)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_he_IL
def test_face_recognize(click, screenDiffChecker):
    click(modal.testing.videostream_close_he)
    click(btn.testing.fr_he)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_he_IL
def test_bottom_camera(click, screenDiffChecker):
    click(modal.testing.videostream_close_he)
    click(btn.testing.bottom_he)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_he_IL
def test_fisheye_camera(click, screenDiffChecker):
    click(modal.testing.videostream_close_he)
    click(btn.testing.fisheye_he)
    assert screenDiffChecker(
        'localization/he_IL/run_testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_he_IL
def test_periphery_statuses(click, screenDiffChecker):
    click(modal.testing.videostream_close_he)
    click(btn.testing.periphery_statuses_he)
    assert screenDiffChecker(
        'localization/he_IL/run_periphery_statuses_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_record_sound_start(click, screenDiffChecker):
    click(modal.testing.periphery_close_he)
    click(btn.testing.record_he)
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
def test_auto_mode_popup(click, typeText, screenDiffChecker):
    click(btn.handler.back_he)
    click(btn.control.restart_he)
    click(modal.restart.yes_he)
    time.sleep(restart)
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_he)
    click(btn.control.auto_mode_he)
    click(btn.handler.back_he)
    assert screenDiffChecker(
        'localization/he_IL/run_automode_popup.png'
    ) is None


@pytest.mark.localization_he_IL
def test_joy_mode_popup(click, typeText, screenDiffChecker):
    time.sleep(modals)
    click(btn.start.control)
    click(modal.pwd.input)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_he)
    click(btn.control.auto_mode_he)
    click(btn.handler.back_he)
    assert screenDiffChecker(
        'localization/he_IL/run_joy_mode_popup.png'
    ) is None


@pytest.mark.localization_he_IL
def test_restore():
    time.sleep(modals)
