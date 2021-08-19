#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.testConfig import modals_timeout
'''
X seconds
'''


@pytest.mark.localization_ru_RU
def test_wrong_pass_modal(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('1234567')
    clickOn('pass_modal_ok')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker(
        'localization/ru_RU/ru_wrong_pass_modal.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_control(clickOn, typeText, screenDiffChecker):
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    assert screenDiffChecker(
        'localization/ru_RU/ru_control.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_connection_open(clickOn, screenDiffChecker):
    clickOn('connection')
    time.sleep(modals_timeout)
    assert screenDiffChecker(
        'localization/ru_RU/ru_connection.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_connection_info_modal(clickOn, screenDiffChecker):
    clickOn('connection_info')
    time.sleep(modals_timeout)
    assert screenDiffChecker(
        'localization/ru_RU/ru_connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_ru_RU
def test_connection_update_modal(clickOn, screenDiffChecker):
    clickOn('connection_info_modal_close')
    clickOn('connection_update')
    time.sleep(2)
    assert screenDiffChecker(
        'localization/ru_RU/ru_connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.localization_ru_RU
def test_connection_wifi_pass_modal(clickOn, screenDiffChecker):
    time.sleep(modals_timeout)
    clickOn('random_wifi')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker(
        'localization/ru_RU/ru_wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_ru_RU
def test_promo_open(clickOn, screenDiffChecker):
    clickOn('wifi_pass_modal_close')
    clickOn('back')
    clickOn('promo')
    assert screenDiffChecker(
        'localization/ru_RU/ru_promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.localization_ru_RU
def test_add_picture_modal(clickOn, screenDiffChecker):
    clickOn('promo_pictures')
    clickOn('promo_pictures')
    clickOn('fs_promo_checkbox1')
    clickOn('promo_add')
    assert screenDiffChecker(
        'localization/ru_RU/ru_add_picture_modal.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_added_picture(clickOn, screenDiffChecker):
    clickOn('promo_modal_yes')
    assert screenDiffChecker(
        'localization/ru_RU/ru_add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_delete_picture_modal(clickOn, screenDiffChecker):
    clickOn('robot_promo_checkbox1')
    clickOn('promo_delete')
    assert screenDiffChecker(
        'localization/ru_RU/ru_delete_picture_modal.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_delete_picture(clickOn, screenDiffChecker):
    clickOn('promo_modal_yes')
    assert screenDiffChecker(
        'localization/ru_RU/ru_delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_printshow(clickOn, screenDiffChecker):
    clickOn('promo_selector')
    clickOn('promo_choose_print')
    assert screenDiffChecker(
        'localization/ru_RU/ru_promo_printshow.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_identification(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('identification')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker(
        'localization/ru_RU/ru_identification.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_charge_app(clickOn, screenDiffChecker):
    clickOn('back')
    clickOn('send_to_charge')
    time.sleep(2)
    assert screenDiffChecker(
        'localization/ru_RU/ru_charge_app.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_phrase_mode_on(clickOn, typeText, screenDiffChecker):
    clickOn('send_to_charge_close')
    time.sleep(modals_timeout)
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('123456')
    clickOn('pass_modal_ok')
    clickOn('phrase_mode')
    assert screenDiffChecker(
        'localization/ru_RU/ru_control_phrase_mode_on.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_phrase_mode_off(clickOn, screenDiffChecker):
    time.sleep(modals_timeout)
    clickOn('phrase_mode')
    assert screenDiffChecker(
        'localization/ru_RU/ru_control_phrase_mode_off.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_volume(joy, node, screenDiffChecker):
    time.sleep(modals_timeout)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/ru_RU/ru_control_volume.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_mic(joy, node, screenDiffChecker):
    time.sleep(modals_timeout)
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    time.sleep(modals_timeout)
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/ru_RU/ru_control_mic.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_restart_modal(clickOn, joy, node, screenDiffChecker):
    time.sleep(modals_timeout)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    time.sleep(modals_timeout)
    clickOn('restart')
    assert screenDiffChecker(
        'localization/ru_RU/ru_restart_modal.png'
    ) is None


@pytest.mark.localization_ru_RU
def test_reset(clickOn):
    clickOn('restart_modal_no')
    clickOn('back')
    time.sleep(modals_timeout)
