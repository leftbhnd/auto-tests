#!/usr/bin/env python
# -*- coding: utf-8 -*-

from main import ClickMsg, FaseMsg
import pytest
import time

def test_main_screen(screenDiffChecker):
    assert screenDiffChecker('main.png') is None


def test_input(node, mouseClick, screenDiffChecker):
    # кнопка получить пропуск
    click_msg = ClickMsg(491, 510, 1)
    mouseClick(click_msg)
    # публикуем лицо в топик
    face_msg = FaseMsg(2, 20, 0, 0.9)
    node.facePub(face_msg)
    # клик в свободную область экрана для сокрытия экранной клавиатуры 
    click_msg = ClickMsg(947, 123, 1)
    mouseClick(click_msg)
    assert screenDiffChecker('input_type.png') is None


def test_save(mouseClick, typeText, screenDiffChecker):
    # клик в инпут фамилия
    click_msg = ClickMsg(431, 245, 1)
    mouseClick(click_msg)
    # набор текста
    typeText(['и','в','а','н','о','в'])
    # клик в инпут имя
    click_msg = ClickMsg(1008, 259, 1)
    mouseClick(click_msg)
    # набор текста
    typeText(['и','в','а','н'])
    # подтвердить
    click_msg = ClickMsg(1222, 419, 1)
    mouseClick(click_msg)
    assert screenDiffChecker('save_db.png') is None


def test_save_db(mouseClick, screenDiffChecker):
    # нет, продолжить
    click_msg = ClickMsg(592, 712, 1)
    mouseClick(click_msg)
    time.sleep(1.5)
    assert screenDiffChecker('success.png') is None
