#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, connection, btn, modal
'''
81.07 seconds
'''


@pytest.mark.localization_el_GR
def test_con_wrong_pass_modal(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('1234567')
    click(modal.pwd_ok)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'localization/el_GR/con_wrong_pass_modal.png'
    ) is None


@pytest.mark.localization_el_GR
def test_control(click, type, screenDiffChecker):
    click(modal.pwd_wrong_input_el)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_wrong_ok_el)
    assert screenDiffChecker(
        'localization/el_GR/con_control.png'
    ) is None


@pytest.mark.localization_el_GR
def test_connection_open(click, screenDiffChecker):
    click(btn.connection)
    time.sleep(connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/el_GR/con_connection.png',
        (0, 40, 890, 150)
    ) is None


@pytest.mark.localization_el_GR
def test_connection_info_modal(click, screenDiffChecker):
    click(btn.connection_info)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/el_GR/con_connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_el_GR
def test_connection_update_modal(click, screenDiffChecker):
    click(modal.connection_info_close)
    click(btn.connection_update)
    time.sleep(connection)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/el_GR/con_connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.localization_el_GR
def test_connection_wifi_pass_modal(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.connection_choose_wifi)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'localization/el_GR/con_wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_el_GR
def test_promo_open(click, screenDiffChecker):
    click(modal.wifi_pwd_close)
    click(btn.back)
    click(btn.promo)
    assert screenDiffChecker(
        'localization/el_GR/con_promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.localization_el_GR
def test_add_picture_modal(click, screenDiffChecker):
    click(btn.promo_pictures)
    click(btn.promo_pictures)
    click(btn.promo_fs_checkbox1)
    click(btn.promo_add)
    assert screenDiffChecker(
        'localization/el_GR/con_add_picture_modal.png'
    ) is None


@pytest.mark.localization_el_GR
def test_added_picture(click, screenDiffChecker):
    click(modal.promo_yes)
    assert screenDiffChecker(
        'localization/el_GR/con_add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_el_GR
def test_delete_picture_modal(click, screenDiffChecker):
    click(btn.promo_robot_checkbox1)
    click(btn.promo_delete)
    assert screenDiffChecker(
        'localization/el_GR/con_delete_picture_modal.png'
    ) is None


@pytest.mark.localization_el_GR
def test_deleted_picture(click, screenDiffChecker):
    click(modal.promo_yes)
    assert screenDiffChecker(
        'localization/el_GR/con_delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_el_GR
def test_printshow(click, screenDiffChecker):
    click(btn.promo_selector)
    click(btn.promo_print)
    assert screenDiffChecker(
        'localization/el_GR/con_promo_printshow.png'
    ) is None


@pytest.mark.localization_el_GR
def test_identification(click, screenDiffChecker):
    click(btn.back)
    click(modal.save_no)
    click(btn.ident)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'localization/el_GR/con_identification.png'
    ) is None


@pytest.mark.localization_el_GR
def test_charge_app(click, screenDiffChecker):
    click(modal.ident_close_el)
    click(btn.charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/el_GR/con_charge_app.png'
    ) is None


@pytest.mark.localization_el_GR
def test_phrase_mode_on(click, type, screenDiffChecker):
    click(btn.charge_app_close)
    time.sleep(modals)
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.phrase_mode)
    assert screenDiffChecker(
        'localization/el_GR/con_phrase_mode_on.png'
    ) is None


@pytest.mark.localization_el_GR
def test_phrase_mode_off(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.phrase_mode)
    assert screenDiffChecker(
        'localization/el_GR/con_phrase_mode_off.png'
    ) is None


@pytest.mark.localization_el_GR
def test_volume(joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/el_GR/con_volume.png'
    ) is None


@pytest.mark.localization_el_GR
def test_mic(joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    time.sleep(modals)
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/el_GR/con_mic.png'
    ) is None


@pytest.mark.localization_el_GR
def test_restart_modal(click, joy, node, screenDiffChecker):
    time.sleep(modals)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    time.sleep(modals)
    click(btn.restart)
    assert screenDiffChecker(
        'localization/el_GR/con_restart_modal.png'
    ) is None


@pytest.mark.localization_el_GR
def test_reset(click):
    click(modal.restart_no)
    click(btn.back)
    time.sleep(modals)
