#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, connection, btn, modal
'''
76.97 seconds
'''


@pytest.mark.localization_he_IL
def test_con_wrong_pass_modal(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('1234567')
    click(modal.inv_pwd_ok)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'localization/he_IL/con_wrong_pass_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_control(click, type, screenDiffChecker):
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.inv_pwd_ok)
    assert screenDiffChecker(
        'localization/he_IL/con_control.png'
    ) is None


@pytest.mark.localization_he_IL
def test_connection_open(click, screenDiffChecker):
    click(btn.inv_connection)
    time.sleep(connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/he_IL/con_connection.png',
        (450, 40, 830, 150)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_info_modal(click, screenDiffChecker):
    click(btn.inv_connection_info)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/he_IL/con_connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_update_modal(click, screenDiffChecker):
    click(modal.inv_connection_info_close)
    click(btn.inv_connection_update)
    time.sleep(connection)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/he_IL/con_connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_wifi_pass_modal(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.connection_choose_wifi)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'localization/he_IL/con_wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_he_IL
def test_promo_open(click, screenDiffChecker):
    click(modal.inv_wifi_pwd_close)
    click(btn.inv_back)
    click(btn.inv_promo)
    assert screenDiffChecker(
        'localization/he_IL/con_promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.localization_he_IL
def test_add_picture_modal(click, screenDiffChecker):
    click(btn.inv_promo_pictures)
    click(btn.inv_promo_pictures)
    click(btn.inv_promo_fs_checkbox1)
    click(btn.inv_promo_add)
    assert screenDiffChecker(
        'localization/he_IL/con_add_picture_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_added_picture(click, screenDiffChecker):
    click(modal.inv_promo_yes)
    assert screenDiffChecker(
        'localization/he_IL/con_add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_he_IL
def test_delete_picture_modal(click, screenDiffChecker):
    click(btn.inv_promo_robot_checkbox1)
    click(btn.inv_promo_delete)
    assert screenDiffChecker(
        'localization/he_IL/con_delete_picture_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_deleted_picture(click, screenDiffChecker):
    click(modal.inv_promo_yes)
    assert screenDiffChecker(
        'localization/he_IL/con_delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_he_IL
def test_printshow(click, screenDiffChecker):
    click(btn.inv_promo_selector)
    click(btn.inv_promo_print)
    assert screenDiffChecker(
        'localization/he_IL/con_promo_printshow.png'
    ) is None


@pytest.mark.localization_he_IL
def test_identification(click, screenDiffChecker):
    click(btn.inv_back)
    click(modal.inv_save_no)
    click(btn.inv_ident)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'localization/he_IL/con_identification.png'
    ) is None


@pytest.mark.localization_he_IL
def test_charge_app(click, screenDiffChecker):
    click(modal.inv_ident_close)
    click(btn.inv_charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/he_IL/con_charge_app.png'
    ) is None


@pytest.mark.localization_he_IL
def test_phrase_mode_on(click, type, screenDiffChecker):
    click(btn.inv_charge_app_close)
    time.sleep(modals)
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.inv_pwd_ok)
    click(btn.inv_phrase_mode)
    assert screenDiffChecker(
        'localization/he_IL/con_phrase_mode_on.png'
    ) is None


@pytest.mark.localization_he_IL
def test_phrase_mode_off(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.inv_phrase_mode)
    assert screenDiffChecker(
        'localization/he_IL/con_phrase_mode_off.png'
    ) is None


@pytest.mark.localization_he_IL
def test_volume(joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/he_IL/con_volume.png'
    ) is None


@pytest.mark.localization_he_IL
def test_mic(joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    time.sleep(modals)
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/he_IL/con_mic.png'
    ) is None


@pytest.mark.localization_he_IL
def test_restart_modal(click, joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    time.sleep(modals)
    click(btn.inv_restart)
    assert screenDiffChecker(
        'localization/he_IL/con_restart_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_reset(click):
    click(modal.inv_restart_no)
    click(btn.inv_back)
    time.sleep(modals)
