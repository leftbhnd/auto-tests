#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly, modals, btn, modal
'''
X seconds
'''


@pytest.mark.localization_he_IL
def test_wrong_pass_modal(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('1234567')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'localization/he_IL/wrong_pass_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_control(clickOn, typeText, screenDiffChecker):
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    assert screenDiffChecker(
        'localization/he_IL/control.png'
    ) is None


@pytest.mark.localization_he_IL
def test_connection_open(clickOn, screenDiffChecker):
    clickOn(btn.inv_connection)
    time.sleep(modals)
    time.sleep(slowly)
    assert screenDiffChecker(
        'localization/he_IL/connection.png',
        (450, 40, 830, 150)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_info_modal(clickOn, screenDiffChecker):
    clickOn(btn.inv_connection_info)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/he_IL/connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_update_modal(clickOn, screenDiffChecker):
    clickOn(modal.inv_connection_info_close)
    clickOn(btn.inv_connection_update)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/he_IL/connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_wifi_pass_modal(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.connection_choose_wifi)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'localization/he_IL/wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_he_IL
def test_promo_open(clickOn, screenDiffChecker):
    clickOn(modal.inv_wifi_pwd_close)
    clickOn(btn.inv_back)
    clickOn(btn.inv_promo)
    assert screenDiffChecker(
        'localization/he_IL/promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.localization_he_IL
def test_add_picture_modal(clickOn, screenDiffChecker):
    clickOn(btn.inv_promo_pictures)
    clickOn(btn.inv_promo_pictures)
    clickOn(btn.inv_promo_fs_checkbox1)
    clickOn(btn.inv_promo_add)
    assert screenDiffChecker(
        'localization/he_IL/add_picture_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_added_picture(clickOn, screenDiffChecker):
    clickOn(modal.inv_promo_yes)
    assert screenDiffChecker(
        'localization/he_IL/add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_he_IL
def test_delete_picture_modal(clickOn, screenDiffChecker):
    clickOn(btn.inv_promo_robot_checkbox1)
    clickOn(btn.inv_promo_delete)
    assert screenDiffChecker(
        'localization/he_IL/delete_picture_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_deleted_picture(clickOn, screenDiffChecker):
    clickOn(modal.inv_promo_yes)
    assert screenDiffChecker(
        'localization/he_IL/delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_he_IL
def test_printshow(clickOn, screenDiffChecker):
    clickOn(btn.inv_promo_selector)
    clickOn(btn.inv_promo_print)
    assert screenDiffChecker(
        'localization/he_IL/promo_printshow.png'
    ) is None


@pytest.mark.localization_he_IL
def test_identification(clickOn, screenDiffChecker):
    clickOn(btn.inv_back)
    clickOn(modal.inv_save_no)
    clickOn(btn.inv_ident)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'localization/he_IL/identification.png'
    ) is None


@pytest.mark.localization_he_IL
def test_charge_app(clickOn, screenDiffChecker):
    clickOn(modal.inv_ident_close)
    clickOn(btn.inv_charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/he_IL/charge_app.png'
    ) is None


@pytest.mark.localization_he_IL
def test_phrase_mode_on(clickOn, typeText, screenDiffChecker):
    clickOn(btn.inv_charge_app_close)
    time.sleep(modals)
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.inv_pwd_ok)
    clickOn(btn.inv_phrase_mode)
    assert screenDiffChecker(
        'localization/he_IL/control_phrase_mode_on.png'
    ) is None


@pytest.mark.localization_he_IL
def test_phrase_mode_off(clickOn, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.inv_phrase_mode)
    assert screenDiffChecker(
        'localization/he_IL/control_phrase_mode_off.png'
    ) is None


@pytest.mark.localization_he_IL
def test_volume(joy, node, screenDiffChecker):
    node.initNode()
    time.sleep(modals)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/he_IL/control_volume.png'
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
        'localization/he_IL/control_mic.png'
    ) is None


@pytest.mark.localization_he_IL
def test_restart_modal(clickOn, joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    time.sleep(modals)
    node.killNode()
    clickOn(btn.inv_restart)
    assert screenDiffChecker(
        'localization/he_IL/restart_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_reset(clickOn):
    clickOn(modal.inv_restart_no)
    clickOn(btn.inv_back)
    time.sleep(modals)
