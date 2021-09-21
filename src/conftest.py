#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import time
import pyautogui as p
import rospy

from datetime import datetime
from PIL import Image, ImageChops
from main import AutoTest
from helpers.config import btn, modal, screens_dir, failed_dir, fast, default, screen_resolution, keyboard
from helpers.messages import JoyCmdMsg


@pytest.fixture
def screenDiffChecker(original_image, coordinates=screen_resolution):
    def _method():
        p.screenshot(
            screens_dir + 'screen.png', region=coordinates
        )
        current = Image.open(
            screens_dir + 'screen.png'
        )
        try:
            original = Image.open(
                screens_dir + original_image
            )
        except IOError:
            p.screenshot(
                screens_dir + original_image, region=coordinates
            )
            original = Image.open(
                screens_dir + original_image
            )
        result = ImageChops.difference(current, original)
        difference = result.getbbox()
        if difference != None:
            result.save(
                failed_dir + 'failed_' + original_image +
                datetime.now().strftime("%d.%m.%Y.%H:%M:%S") + '.png'
            )
        return difference
    return _method


@pytest.fixture
def dNd(msg):
    def _method():
        p.leftClick(msg.startX, msg.startY, 0.5)
        p.dragTo(msg.finishX, msg.finishY, 0.5, button='left')
    return _method


@pytest.fixture
def clickOn(button):
    def _method():
        x = button.value[0]
        y = button.value[1]
        p.leftClick(x, y)
        time.sleep(default)
    return _method


@pytest.fixture
def typeText(symbols):
    def _method():
        for symbol in symbols:
            x = keyboard[symbol][0]
            y = keyboard[symbol][1]
            p.leftClick(x, y)
    return _method


@pytest.fixture
def openPwdModal():
    def _method():
        for i in range(5):
            p.leftClick(50, 50)
        time.sleep(default)
    return _method


@pytest.fixture
def openServiceMenu():
    def _method():
        for i in range(5):
            p.leftClick(50, 50)
        time.sleep(default)
        clickOn(modal.pwd_input)
        clickOn(btn.choose_numbers)
        typeText('123456')
        clickOn(modal.pwd_ok)
    return _method


@pytest.fixture
def node():
    rospy.init_node('autotest')
    node = AutoTest()
    time.sleep(default)
    return node


@pytest.fixture
def joy():
    joy = JoyCmdMsg()
    time.sleep(fast)
    return joy
