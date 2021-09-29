#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, default, modals, connection
'''
80.85 seconds
'''


@pytest.mark.localization_pt_PT
def test_con_wrong_pass_modal(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('1234567')
    click(modal.pwd.ok)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/pt_PT/con_wrong_pass_modal.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_control(click, typeText, screenDiffChecker):
    click(modal.pwd.wr_input_pt)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.wr_ok_pt)
    assert screenDiffChecker(
        'localization/pt_PT/con_control.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_connection_open(click, screenDiffChecker):
    click(btn.control.connection)
    time.sleep(connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/pt_PT/con_connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.localization_pt_PT
def test_connection_info_modal(click, screenDiffChecker):
    click(btn.connection.info)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/pt_PT/con_connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_pt_PT
def test_connection_update_modal(click, screenDiffChecker):
    click(modal.connection_info.close)
    click(btn.connection.update)
    time.sleep(connection)
    time.sleep(default)
    assert screenDiffChecker(
        'localization/pt_PT/con_connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.localization_pt_PT
def test_connection_wifi_pass_modal(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.connection.choose_wifi)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/pt_PT/con_wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_pt_PT
def test_promo_open(click, screenDiffChecker):
    click(modal.wifi_pwd.close)
    click(btn.handler.back)
    click(btn.control.promo)
    assert screenDiffChecker(
        'localization/pt_PT/con_promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.localization_pt_PT
def test_add_picture_modal(click, screenDiffChecker):
    click(btn.promo.pictures)
    click(btn.promo.pictures)
    click(btn.promo.fs_checkbox1)
    click(btn.promo.add)
    assert screenDiffChecker(
        'localization/pt_PT/con_add_picture_modal.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_added_picture(click, screenDiffChecker):
    click(modal.promo.yes)
    assert screenDiffChecker(
        'localization/pt_PT/con_add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_delete_picture_modal(click, screenDiffChecker):
    click(btn.promo.robot_checkbox1)
    click(btn.promo.remove)
    assert screenDiffChecker(
        'localization/pt_PT/con_delete_picture_modal.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_deleted_picture(click, screenDiffChecker):
    click(modal.promo.yes)
    assert screenDiffChecker(
        'localization/pt_PT/con_delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_printshow(click, screenDiffChecker):
    click(btn.promo.selector)
    click(btn.promo.printshow)
    assert screenDiffChecker(
        'localization/pt_PT/con_promo_printshow.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_identification(click, screenDiffChecker):
    click(btn.handler.back)
    click(modal.save.no)
    click(btn.control.ident)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/pt_PT/con_identification.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_charge_app(click, screenDiffChecker):
    click(modal.ident.close_pt)
    click(btn.control.charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/pt_PT/con_charge_app.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_phrase_mode_on(click, typeText, screenDiffChecker):
    click(btn.control.charge_app_close)
    click(btn.handler.reset)
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.phrase_mode)
    assert screenDiffChecker(
        'localization/pt_PT/con_phrase_mode_on.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_phrase_mode_off(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.control.phrase_mode)
    assert screenDiffChecker(
        'localization/pt_PT/con_phrase_mode_off.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_volume(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/pt_PT/con_volume.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_mic(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    click(btn.handler.reset)
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/pt_PT/con_mic.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_restart_modal(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    click(btn.handler.reset)
    click(btn.control.restart)
    assert screenDiffChecker(
        'localization/pt_PT/con_restart_modal.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_auto_mode_popup(click, screenDiffChecker):
    click(modal.restart.no)
    click(btn.control.auto_mode)
    click(btn.handler.back)
    assert screenDiffChecker(
        'localization/pt_PT/con_automode_popup.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_joy_mode_popup(click, typeText, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.auto_mode)
    click(btn.handler.back)
    assert screenDiffChecker(
        'localization/pt_PT/con_joy_mode_popup.png'
    ) is None


@pytest.mark.localization_pt_PT
def test_reset(click):
    click(btn.handler.reset)
