#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, connection
'''
80.54 seconds
'''


@pytest.mark.localization_he_IL
def test_con_wrong_pass_modal(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('1234567')
    click(modal.pwd.ok_he)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/he_IL/con_wrong_pass_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_control(click, typeText, screenDiffChecker):
    click(modal.pwd.input)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_he)
    assert screenDiffChecker(
        'localization/he_IL/con_control.png'
    ) is None


@pytest.mark.localization_he_IL
def test_connection_open(click, screenDiffChecker):
    click(btn.control.connection_he)
    assert screenDiffChecker(
        'localization/he_IL/con_connection_open.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_update_modal(screenDiffChecker):
    time.sleep(connection)
    assert screenDiffChecker(
        'localization/he_IL/con_connection_update_modal.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_he_IL
def test_connection(screenDiffChecker):
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/he_IL/con_connection.png',
        (450, 40, 830, 150)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_wifi_pass_modal(click, screenDiffChecker):
    click(btn.connection.choose_wifi)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/he_IL/con_wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_info_modal(click, screenDiffChecker):
    click(modal.wifi_pwd.close_he)
    click(btn.connection.info_he)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/he_IL/con_connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_he_IL
def test_connection_update(click, screenDiffChecker):
    click(modal.connection_info.close_he)
    click(btn.connection.update_he)
    assert screenDiffChecker(
        'localization/he_IL/con_connection_update.png',
        (0, 40, 1280, 115)
    ) is None


@pytest.mark.localization_he_IL
def test_promo_open(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.handler.back_he)
    click(btn.control.promo_he)
    assert screenDiffChecker(
        'localization/he_IL/con_promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.localization_he_IL
def test_add_picture_modal(click, screenDiffChecker):
    click(btn.promo.pictures_he)
    click(btn.promo.pictures_he)
    click(btn.promo.fs_checkbox1_he)
    click(btn.promo.add_he)
    assert screenDiffChecker(
        'localization/he_IL/con_add_picture_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_added_picture(click, screenDiffChecker):
    click(modal.promo.yes_he)
    assert screenDiffChecker(
        'localization/he_IL/con_add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_he_IL
def test_delete_picture_modal(click, screenDiffChecker):
    click(btn.promo.robot_checkbox1_he)
    click(btn.promo.remove_he)
    assert screenDiffChecker(
        'localization/he_IL/con_delete_picture_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_deleted_picture(click, screenDiffChecker):
    click(modal.promo.yes_he)
    assert screenDiffChecker(
        'localization/he_IL/con_delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_he_IL
def test_printshow(click, screenDiffChecker):
    click(btn.promo.selector_he)
    click(btn.promo.printshow_he)
    assert screenDiffChecker(
        'localization/he_IL/con_promo_printshow.png'
    ) is None


@pytest.mark.localization_he_IL
def test_identification(click, screenDiffChecker):
    click(btn.handler.back_he)
    click(modal.save.no_he)
    click(btn.control.ident_he)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/he_IL/con_identification.png'
    ) is None


@pytest.mark.localization_he_IL
def test_charge_app(click, screenDiffChecker):
    click(modal.ident.close_he)
    click(btn.control.charge_app_he)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/he_IL/con_charge_app.png'
    ) is None


@pytest.mark.localization_he_IL
def test_phrase_mode_on(click, typeText, screenDiffChecker):
    click(btn.control.charge_app_close_he)
    click(btn.handler.reset)
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_he)
    click(btn.control.phrase_mode_he)
    assert screenDiffChecker(
        'localization/he_IL/con_phrase_mode_on.png'
    ) is None


@pytest.mark.localization_he_IL
def test_phrase_mode_off(click, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.control.phrase_mode_he)
    assert screenDiffChecker(
        'localization/he_IL/con_phrase_mode_off.png'
    ) is None


@pytest.mark.localization_he_IL
def test_volume(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/he_IL/con_volume.png'
    ) is None


@pytest.mark.localization_he_IL
def test_mic(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    click(btn.handler.reset)
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/he_IL/con_mic.png'
    ) is None


@pytest.mark.localization_he_IL
def test_restart_modal(click, screenDiffChecker, joy, node):
    click(btn.handler.reset)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    click(btn.handler.reset)
    click(btn.control.restart_he)
    assert screenDiffChecker(
        'localization/he_IL/con_restart_modal.png'
    ) is None


@pytest.mark.localization_he_IL
def test_auto_mode_popup(click, screenDiffChecker):
    click(modal.restart.no_he)
    click(btn.control.auto_mode_he)
    click(btn.handler.back_he)
    assert screenDiffChecker(
        'localization/he_IL/con_automode_popup.png'
    ) is None


@pytest.mark.localization_he_IL
def test_joy_mode_popup(click, typeText, screenDiffChecker):
    click(btn.handler.reset)
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok_he)
    click(btn.control.auto_mode_he)
    click(btn.handler.back_he)
    assert screenDiffChecker(
        'localization/he_IL/con_joy_mode_popup.png'
    ) is None


@pytest.mark.localization_he_IL
def test_reset(click):
    click(btn.handler.reset)
