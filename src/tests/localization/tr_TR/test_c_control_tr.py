#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly, modals, connection, btn, modal
'''
82.67 seconds
'''


@pytest.mark.localization_tr_TR
def test_con_wrong_pass_modal(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('1234567')
    clickOn(modal.pwd_ok)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'localization/tr_TR/con_wrong_pass_modal.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_control(clickOn, typeText, screenDiffChecker):
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    assert screenDiffChecker(
        'localization/tr_TR/con_control.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_connection_open(clickOn, screenDiffChecker):
    clickOn(btn.connection)
    time.sleep(connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/tr_TR/con_connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.localization_tr_TR
def test_connection_info_modal(clickOn, screenDiffChecker):
    clickOn(btn.connection_info)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/tr_TR/con_connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_tr_TR
def test_connection_update_modal(clickOn, screenDiffChecker):
    clickOn(modal.connection_info_close)
    clickOn(btn.connection_update)
    time.sleep(connection)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/tr_TR/con_connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.localization_tr_TR
def test_connection_wifi_pass_modal(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.connection_choose_wifi)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'localization/tr_TR/con_wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_tr_TR
def test_promo_open(clickOn, screenDiffChecker):
    clickOn(modal.wifi_pwd_close)
    clickOn(btn.back)
    clickOn(btn.promo)
    assert screenDiffChecker(
        'localization/tr_TR/con_promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.localization_tr_TR
def test_add_picture_modal(clickOn, screenDiffChecker):
    clickOn(btn.promo_pictures)
    clickOn(btn.promo_pictures)
    clickOn(btn.promo_fs_checkbox1)
    clickOn(btn.promo_add)
    assert screenDiffChecker(
        'localization/tr_TR/con_add_picture_modal.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_added_picture(clickOn, screenDiffChecker):
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'localization/tr_TR/con_add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_delete_picture_modal(clickOn, screenDiffChecker):
    clickOn(btn.promo_robot_checkbox1)
    clickOn(btn.promo_delete)
    assert screenDiffChecker(
        'localization/tr_TR/con_delete_picture_modal.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_deleted_picture(clickOn, screenDiffChecker):
    clickOn(modal.promo_yes)
    assert screenDiffChecker(
        'localization/tr_TR/con_delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_printshow(clickOn, screenDiffChecker):
    clickOn(btn.promo_selector)
    clickOn(btn.promo_print)
    assert screenDiffChecker(
        'localization/tr_TR/con_promo_printshow.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_identification(clickOn, screenDiffChecker):
    clickOn(btn.back)
    clickOn(modal.save_no)
    clickOn(btn.ident)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'localization/tr_TR/con_identification.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_charge_app(clickOn, screenDiffChecker):
    clickOn(modal.ident_close_tr)
    clickOn(btn.charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/tr_TR/con_charge_app.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_phrase_mode_on(clickOn, typeText, screenDiffChecker):
    clickOn(btn.charge_app_close)
    time.sleep(modals)
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.phrase_mode)
    assert screenDiffChecker(
        'localization/tr_TR/con_phrase_mode_on.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_phrase_mode_off(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.phrase_mode)
    assert screenDiffChecker(
        'localization/tr_TR/con_phrase_mode_off.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_volume(joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/tr_TR/con_volume.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_mic(joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    time.sleep(modals)
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/tr_TR/con_mic.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_restart_modal(clickOn, joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    time.sleep(modals)
    clickOn(btn.restart)
    assert screenDiffChecker(
        'localization/tr_TR/con_restart_modal.png'
    ) is None


@pytest.mark.localization_tr_TR
def test_reset(clickOn):
    clickOn(modal.restart_no)
    clickOn(btn.back)
    time.sleep(modals)
