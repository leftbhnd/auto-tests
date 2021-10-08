#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, connection
'''
66.48 seconds
'''


@pytest.mark.localization_el_GR
def test_con_wrong_pass_modal(click, typeText, screenDiffChecker):
    click(btn.start.control)
    typeText(1234567)
    click(modal.pwd.ok)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/el_GR/con_wrong_pass_modal.png',
        (365, 160, 545, 200)
    ) is None


@pytest.mark.localization_el_GR
def test_control(click, typeText, screenDiffChecker):
    click(modal.pwd.wr_input_el)
    typeText(123456)
    click(modal.pwd.wr_ok_el)
    assert screenDiffChecker(
        'localization/el_GR/con_control.png'
    ) is None


@pytest.mark.localization_el_GR
def test_connection_open(click, screenDiffChecker):
    click(btn.control.connection)
    assert screenDiffChecker(
        'localization/el_GR/con_connection_open.png',
        (0, 40, 1280, 110)
    ) is None


@pytest.mark.localization_el_GR
def test_connection_update_modal(screenDiffChecker):
    time.sleep(connection)
    assert screenDiffChecker(
        'localization/el_GR/con_connection_update_modal.png',
        (0, 40, 1280, 110)
    ) is None


@pytest.mark.localization_el_GR
def test_connection(screenDiffChecker):
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/el_GR/con_connection.png',
        (0, 40, 890, 150)
    ) is None


@pytest.mark.localization_el_GR
def test_connection_wifi_pass_modal(click, screenDiffChecker):
    click(btn.connection.choose_wifi)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/el_GR/con_wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_el_GR
def test_connection_info_modal(click, screenDiffChecker):
    click(modal.wifi_pwd.close)
    click(btn.connection.info)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/el_GR/con_connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_el_GR
def test_connection_update(click, screenDiffChecker):
    click(modal.connection_info.close)
    click(btn.connection.update)
    assert screenDiffChecker(
        'localization/el_GR/con_connection_update.png',
        (0, 40, 1280, 110)
    ) is None


@pytest.mark.localization_el_GR
def test_add_picture_modal(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.handler.back)
    click(btn.control.promo)
    click(btn.promo.pictures)
    click(btn.promo.pictures)
    click(btn.promo.fs_checkbox1)
    click(btn.promo.add)
    assert screenDiffChecker(
        'localization/el_GR/con_add_picture_modal.png'
    ) is None


@pytest.mark.localization_el_GR
def test_added_picture(click, screenDiffChecker):
    click(modal.promo.yes)
    assert screenDiffChecker(
        'localization/el_GR/con_add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_el_GR
def test_delete_picture_modal(click, screenDiffChecker):
    click(btn.promo.robot_checkbox1)
    click(btn.promo.remove)
    assert screenDiffChecker(
        'localization/el_GR/con_delete_picture_modal.png'
    ) is None


@pytest.mark.localization_el_GR
def test_deleted_picture(click, screenDiffChecker):
    click(modal.promo.yes)
    assert screenDiffChecker(
        'localization/el_GR/con_delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_el_GR
def test_printshow(click, screenDiffChecker):
    click(btn.promo.selector)
    click(btn.promo.printshow)
    assert screenDiffChecker(
        'localization/el_GR/con_promo_printshow.png'
    ) is None


@pytest.mark.localization_el_GR
def test_identification(click, screenDiffChecker):
    click(btn.handler.back)
    click(modal.save.no)
    click(btn.control.ident)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/el_GR/con_identification.png',
        (200, 275, 880, 240)
    ) is None


@pytest.mark.localization_el_GR
def test_charge_app(click, screenDiffChecker):
    click(modal.ident.close_el)
    click(btn.control.charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/el_GR/con_charge_app.png'
    ) is None


@pytest.mark.localization_el_GR
def test_phrase_mode_on(click, typeText, screenDiffChecker):
    click(btn.control.charge_app_close)
    click(btn.handler.reset)
    click(btn.start.control)
    typeText(123456)
    click(modal.pwd.ok)
    click(btn.control.phrase_mode)
    assert screenDiffChecker(
        'localization/el_GR/con_phrase_mode_on.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_el_GR
def test_phrase_mode_off(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.control.phrase_mode)
    assert screenDiffChecker(
        'localization/el_GR/con_phrase_mode_off.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_el_GR
def test_volume(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/el_GR/con_volume.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_el_GR
def test_mic(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    click(btn.handler.reset)
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/el_GR/con_mic.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_el_GR
def test_restart_modal(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    click(btn.handler.reset)
    click(btn.control.restart)
    assert screenDiffChecker(
        'localization/el_GR/con_restart_modal.png',
        (360, 310, 560, 170)
    ) is None


@pytest.mark.localization_el_GR
def test_auto_mode_popup(click, screenDiffChecker):
    click(modal.restart.no)
    click(btn.control.auto_mode)
    click(btn.handler.back)
    assert screenDiffChecker(
        'localization/el_GR/con_automode_popup.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_el_GR
def test_joy_mode_popup(click, typeText, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.start.control)
    typeText(123456)
    click(modal.pwd.ok)
    click(btn.control.auto_mode)
    click(btn.handler.back)
    assert screenDiffChecker(
        'localization/el_GR/con_joy_mode_popup.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_el_GR
def test_reset(click):
    click(btn.handler.reset)
