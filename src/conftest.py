#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import time
import pyautogui
import rospy

from PIL import Image, ImageChops
from pymouse import PyMouse
from main import AutoTest
from helpers.helpers import kb_symbols_dict, buttons_dict
from helpers.test_config import screens_dir, failed_dir, faster_timeout, default_timeout
from helpers.messages import JoyCmdMsg


m = PyMouse()


@pytest.fixture
def screenDiffChecker():
    def _method(original_image, coordinates=(0, 40, 1280, 800)):
        pyautogui.screenshot(
            screens_dir + 'screen.png', region=coordinates
        )
        current = Image.open(
            screens_dir + 'screen.png'
        )
        original = Image.open(
            screens_dir + original_image
        )
        result = ImageChops.difference(current, original)
        difference = result.getbbox()
        if difference != None:
            result.save(
                failed_dir + 'failed_' + original_image
            )
            # pyautogui.screenshot(
            #     screens_dir + original_image, region=coordinates
            # )
            return difference
    return _method


@pytest.fixture
def pressAndMove():
    def _method(msg):
        m.press(msg.startX, msg.startY, 1)
        time.sleep(default_timeout)
        m.release(msg.finishX, msg.finishY, 1)
        time.sleep(default_timeout)
    return _method


@pytest.fixture
def clickOn():
    def _method(button):
        x = buttons_dict[button][0]
        y = buttons_dict[button][1]
        m.click(x, y, 1)
        time.sleep(default_timeout)
    return _method


@pytest.fixture
def openPasswordModal():
    def _method():
        for i in range(5):
            m.click(50, 50, 1)
            time.sleep(faster_timeout)
        time.sleep(default_timeout)
    return _method


@pytest.fixture
def typeText():
    def _method(symbols):
        for symbol in symbols:
            x = kb_symbols_dict[symbol][0]
            y = kb_symbols_dict[symbol][1]
            m.click(x, y, 1)
            time.sleep(faster_timeout)
    return _method


@pytest.fixture
def node():
    rospy.init_node('autotest')
    node = AutoTest()
    time.sleep(default_timeout)
    return node


@pytest.fixture
def joy():
    joy = JoyCmdMsg()
    time.sleep(default_timeout)
    return joy
