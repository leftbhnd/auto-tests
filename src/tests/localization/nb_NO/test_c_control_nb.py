#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, connection
'''
80.72 seconds
'''


@pytest.mark.localization_nb_NO
def test_con_wrong_pass_modal(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('1234567')
    click(modal.pwd.ok)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/nb_NO/con_wrong_pass_modal.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_control(click, typeText, screenDiffChecker):
    click(modal.pwd.input)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    assert screenDiffChecker(
        'localization/nb_NO/con_control.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_connection_open(click, screenDiffChecker):
    click(btn.control.connection)
    time.sleep(connection)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/nb_NO/con_connection.png',
        (0, 40, 920, 150)
    ) is None


@pytest.mark.localization_nb_NO
def test_connection_info_modal(click, screenDiffChecker):
    click(btn.connection.info)
    time.sleep(modals)
    assert screenDiffChecker(
        'localization/nb_NO/con_connection_info_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_nb_NO
def test_connection_update_modal(click, screenDiffChecker):
    click(modal.connection_info.close)
    click(btn.connection.update)
    time.sleep(connection)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/nb_NO/con_connection_update_modal.png',
        (0, 40, 1280, 120)
    ) is None


@pytest.mark.localization_nb_NO
def test_connection_wifi_pass_modal(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.connection.choose_wifi)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/nb_NO/con_wifi_pass_modal.png',
        (365, 292, 548, 212)
    ) is None


@pytest.mark.localization_nb_NO
def test_promo_open(click, screenDiffChecker):
    click(modal.wifi_pwd.close)
    click(btn.handler.back)
    click(btn.control.promo)
    assert screenDiffChecker(
        'localization/nb_NO/con_promo.png',
        (0, 40, 1280, 100)
    ) is None


@pytest.mark.localization_nb_NO
def test_add_picture_modal(click, screenDiffChecker):
    click(btn.promo.pictures)
    click(btn.promo.pictures)
    click(btn.promo.fs_checkbox1)
    click(btn.promo.add)
    assert screenDiffChecker(
        'localization/nb_NO/con_add_picture_modal.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_added_picture(click, screenDiffChecker):
    click(modal.promo.yes)
    assert screenDiffChecker(
        'localization/nb_NO/con_add_picture_slideshow.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_delete_picture_modal(click, screenDiffChecker):
    click(btn.promo.robot_checkbox1)
    click(btn.promo.remove)
    assert screenDiffChecker(
        'localization/nb_NO/con_delete_picture_modal.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_deleted_picture(click, screenDiffChecker):
    click(modal.promo.yes)
    assert screenDiffChecker(
        'localization/nb_NO/con_delete_picture_slideshow.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_printshow(click, screenDiffChecker):
    click(btn.promo.selector)
    click(btn.promo.printshow)
    assert screenDiffChecker(
        'localization/nb_NO/con_promo_printshow.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_identification(click, screenDiffChecker):
    click(btn.handler.back)
    click(modal.save.no)
    click(btn.control.ident)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'localization/nb_NO/con_identification.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_charge_app(click, screenDiffChecker):
    click(modal.ident.close_nb)
    click(btn.control.charge_app)
    time.sleep(2)
    assert screenDiffChecker(
        'localization/nb_NO/con_charge_app.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_phrase_mode_on(click, typeText, screenDiffChecker):
    click(btn.control.charge_app_close)
    time.sleep(modals)
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.phrase_mode)
    assert screenDiffChecker(
        'localization/nb_NO/con_phrase_mode_on.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_phrase_mode_off(click, screenDiffChecker):
    time.sleep(modals)
    click(btn.control.phrase_mode)
    assert screenDiffChecker(
        'localization/nb_NO/con_phrase_mode_off.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_volume(screenDiffChecker, joy, node):
    time.sleep(modals)
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/nb_NO/con_volume.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_mic(screenDiffChecker, joy, node):
    time.sleep(modals)
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    time.sleep(modals)
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    assert screenDiffChecker(
        'localization/nb_NO/con_mic.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_restart_modal(click, screenDiffChecker, joy, node):
    time.sleep(modals)
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    time.sleep(modals)
    click(btn.control.restart)
    assert screenDiffChecker(
        'localization/nb_NO/con_restart_modal.png'
    ) is None


@pytest.mark.localization_nb_NO
def test_reset(click):
    click(modal.restart.no)
    click(btn.handler.back)
    time.sleep(modals)
