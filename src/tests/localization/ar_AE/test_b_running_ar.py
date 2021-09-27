#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, default, slowly, modals, running, restart
'''
148.49 seconds
'''


@pytest.mark.localization_ar_AE
def test_no_connection_modal(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.lang)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_ae)
    click(btn.control.answers_log_ae)
    click(btn.control.restart_ae)
    click(modal.restart.yes_ae)
    time.sleep(35)
    click(btn.start.play)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/run_no_connection_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_radius_modal(click, screenDiffChecker):
    click(modal.no_connection.yes_ae)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/run_radius_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_check_run_state(click, screenDiffChecker):
    click(modal.radius.yes_ae)
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
def test_answer_log(click, screenDiffChecker, node):
    time.sleep(running)
    click(modal.ans_log.clear_ae)
    node.cancelSpeechPub()
    node.asrPub('حكم اختبار مجرفة')
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/ar_AE/run_test_answers_log.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_ar_AE
def test_speech_settings(click, screenDiffChecker):
    click(modal.ans_log.close_ae)
    click(btn.gui.speech_settings_ae)
    assert screenDiffChecker(
        'localization/ar_AE/run_speech_settings.png',
        (0, 40, 1280, 660)
    ) is None


@pytest.mark.localization_ar_AE
def test_testing_script(click, typeText, openPwdModal, screenDiffChecker):
    click(modal.speech_settings.close_ae)
    openPwdModal()
    click(btn.kb.lang)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_ae)
    click(btn.control.testing_ae)
    time.sleep(modals)
    click(btn.testing.hand_right_ae)
    time.sleep(default)
    assert screenDiffChecker(
        'localization/ar_AE/run_script_is_running.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_main_camera(click, screenDiffChecker, node):
    node.cancelScriptPub()
    time.sleep(modals)
    click(btn.testing.main_camera_ae)
    assert screenDiffChecker(
        'localization/ar_AE/run_testing_main_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ar_AE
def test_face_recognize(click, screenDiffChecker):
    click(modal.testing.videostream_close_ae)
    click(btn.testing.fr_ae)
    assert screenDiffChecker(
        'localization/ar_AE/run_testing_face_recognize_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ar_AE
def test_bottom_camera(click, screenDiffChecker):
    click(modal.testing.videostream_close_ae)
    click(btn.testing.bottom_ae)
    assert screenDiffChecker(
        'localization/ar_AE/run_testing_bottom_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ar_AE
def test_fisheye_camera(click, screenDiffChecker):
    click(modal.testing.videostream_close_ae)
    click(btn.testing.fisheye_ae)
    assert screenDiffChecker(
        'localization/ar_AE/run_testing_fisheye_camera_header.png',
        (0, 40, 1280, 60)
    ) is None


@pytest.mark.localization_ar_AE
def test_periphery_statuses(click, screenDiffChecker):
    click(modal.testing.videostream_close_ae)
    click(btn.testing.periphery_statuses_ae)
    assert screenDiffChecker(
        'localization/ar_AE/run_periphery_statuses_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_record_sound_start(click, screenDiffChecker):
    click(modal.testing.periphery_close_ae)
    click(btn.testing.record_ae)
    assert screenDiffChecker(
        'localization/ar_AE/run_testing_record_sound_start.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_record_sound_finish(screenDiffChecker):
    time.sleep(10)
    assert screenDiffChecker(
        'localization/ar_AE/run_testing_record_sound_finish.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_restore(click):
    click(btn.handler.back_ae)
    click(btn.control.restart_ae)
    click(modal.restart.yes_ae)
    time.sleep(restart)
