#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import time
import pyautogui
import rospy

from PIL import Image, ImageChops
from pymouse import PyMouse
from main import AutoTest
from helpers.helpers import kb_symbols_dict, buttons_dict, screens_dir, faster_timeout, default_timeout
from helpers.messages import JoyCmdMsg


m = PyMouse()


@pytest.fixture
def mouseClick():
    def _method(msg):
        m.click(msg.x, msg.y, 1)
        time.sleep(default_timeout)
    return _method


@pytest.fixture
def screenDiffChecker():
    def _method(original_image, coordinates=(0, 40, 1280, 800)):
        pyautogui.screenshot(
            screens_dir + 'screen.png', region=coordinates
        )
        current = Image.open(screens_dir + 'screen.png')
        original = Image.open(
            screens_dir + original_image
        )
        difference = ImageChops.difference(current, original).getbbox()
        return difference
    return _method


@pytest.fixture
def pressAndMove():
    def _method(twoPointsList):
        startX = twoPointsList[0][0]
        startY = twoPointsList[0][1]
        finishX = twoPointsList[1][0]
        finishY = twoPointsList[1][1]
        m.press(startX, startY, 1)
        time.sleep(default_timeout)
        m.release(finishX, finishY, 1)
        time.sleep(default_timeout)
    return _method


@pytest.fixture
def clickOn():
    def _method(button):
        m.click(buttons_dict[button][0], buttons_dict[button][1], 1)
        time.sleep(default_timeout)
    return _method


@pytest.fixture
def openPasswordModal():
    def _method():
        m.click(50, 50, 1)
        time.sleep(faster_timeout)
        m.click(50, 50, 1)
        time.sleep(faster_timeout)
        m.click(50, 50, 1)
        time.sleep(faster_timeout)
        m.click(50, 50, 1)
        time.sleep(faster_timeout)
        m.click(50, 50, 1)
        time.sleep(faster_timeout)
    return _method


@pytest.fixture
def typeText():
    def _method(array_of_letters):
        for symbol in array_of_letters:
            m.click(kb_symbols_dict[symbol][0], kb_symbols_dict[symbol][1], 1)
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
