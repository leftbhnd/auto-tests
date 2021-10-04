#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, connection
'''
68.55 seconds
'''


@pytest.mark.localization_ar_AE
def test_con_wrong_pass_modal(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.lang)
    typeText(1234567)
    click(modal.pwd.ok_ae)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/ar_AE/con_wrong_pass_modal.png',
        (365, 160, 545, 200)
    ) is None


@pytest.mark.localization_ar_AE
def test_control(click, typeText, screenDiffChecker):
    click(modal.pwd.input)
    click(btn.kb.lang)
    typeText(123456)
    click(modal.pwd.ok_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_control.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_connection_open(click, screenDiffChecker):
    click(btn.control.connection_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_connection_open.png',
        (0, 40, 1280, 110)
    ) is None


@pytest.mark.localization_ar_AE
def test_connection_update_modal(screenDiffChecker):
    time.sleep(connection)
    assert screenDiffChecker(
        'localization/ar_AE/con_connection_update_modal.png',
        (0, 40, 1280, 110)
    ) is None


@pytest.mark.localization_ar_AE
def test_connection(screenDiffChecker):
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/ar_AE/con_connection.png',
        (455, 40, 825, 150)
    ) is None


@pytest.mark.localization_ar_AE
def test_connection_wifi_pass_modal(click, screenDiffChecker):
    click(btn.connection.choose_wifi)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/ar_AE/con_wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_ar_AE
def test_connection_info_modal(click, screenDiffChecker):
    click(modal.wifi_pwd.close_ae)
    click(btn.connection.info_ae)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/ar_AE/con_connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_ar_AE
def test_connection_update(click, screenDiffChecker):
    click(modal.connection_info.close_ae)
    click(btn.connection.update_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_connection_update.png',
        (0, 40, 1280, 110)
    ) is None


@pytest.mark.localization_ar_AE
def test_promo_open(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.handler.back_ae)
    click(btn.control.promo_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.localization_ar_AE
def test_add_picture_modal(click, screenDiffChecker):
    click(btn.promo.pictures_ae)
    click(btn.promo.pictures_ae)
    click(btn.promo.fs_checkbox1_ae)
    click(btn.promo.add_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_add_picture_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_added_picture(click, screenDiffChecker):
    click(modal.promo.yes_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_delete_picture_modal(click, screenDiffChecker):
    click(btn.promo.robot_checkbox1_ae)
    click(btn.promo.remove_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_delete_picture_modal.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_deleted_picture(click, screenDiffChecker):
    click(modal.promo.yes_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_printshow(click, screenDiffChecker):
    click(btn.promo.selector_ae)
    click(btn.promo.printshow_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_promo_printshow.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_identification(click, screenDiffChecker):
    click(btn.handler.back_ae)
    click(modal.save.no_ae)
    click(btn.control.ident_ae)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/ar_AE/con_identification.png',
        (370, 275, 545, 250)
    ) is None


@pytest.mark.localization_ar_AE
def test_charge_app(click, screenDiffChecker):
    click(modal.ident.close_ae)
    click(btn.control.charge_app_ae)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/ar_AE/con_charge_app.png'
    ) is None


@pytest.mark.localization_ar_AE
def test_phrase_mode_on(click, typeText, screenDiffChecker):
    click(btn.control.charge_app_close_ae)
    click(btn.handler.reset)
    click(btn.start.control)
    click(btn.kb.lang)
    typeText(123456)
    click(modal.pwd.ok_ae)
    click(btn.control.phrase_mode_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_phrase_mode_on.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_ar_AE
def test_phrase_mode_off(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.control.phrase_mode_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_phrase_mode_off.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_ar_AE
def test_volume(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/ar_AE/con_volume.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_ar_AE
def test_mic(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    click(btn.handler.reset)
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/ar_AE/con_mic.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_ar_AE
def test_restart_modal(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    click(btn.handler.reset)
    click(btn.control.restart_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_restart_modal.png',
        (370, 310, 540, 180)
    ) is None


@pytest.mark.localization_ar_AE
def test_auto_mode_popup(click, screenDiffChecker):
    click(modal.restart.no_ae)
    click(btn.control.auto_mode_ae)
    click(btn.handler.back_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_automode_popup.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_ar_AE
def test_joy_mode_popup(click, typeText, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.start.control)
    click(btn.kb.lang)
    typeText(123456)
    click(modal.pwd.ok_ae)
    click(btn.control.auto_mode_ae)
    click(btn.handler.back_ae)
    assert screenDiffChecker(
        'localization/ar_AE/con_joy_mode_popup.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_ar_AE
def test_reset(click):
    click(btn.handler.reset)
