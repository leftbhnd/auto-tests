#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import time
import pyautogui
import rospy

from datetime import datetime
from PIL import Image, ImageChops
from pymouse import PyMouse
from main import AutoTest
from helpers.config import screens_dir, failed_dir, fast, default, slowly, screen_resolution, keyboard
from helpers.messages import JoyCmdMsg

p = pyautogui()
m = PyMouse()


@pytest.fixture
def screenDiffChecker():
    def _method(original_image, coordinates=screen_resolution):
        pyautogui.screenshot(
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
            pyautogui.screenshot(
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
def dNd():
    def _method(msg):
        p.leftClick(msg.startX, msg.startY, 0.5)
        #pyautogui.dragTo(msg.startX, msg.startY, button='left')
        p.dragTo(msg.finishX, msg.finishY, 0.5, button='left')
        # m.press(msg.startX, msg.startY, 1)
        # time.sleep(default)
        # m.release(msg.finishX, msg.finishY, 1)
        # time.sleep(default)
    return _method


@pytest.fixture
def clickOn():
    def _method(button):
        x = button.value[0]
        y = button.value[1]
        m.click(x, y, 1)
        time.sleep(default)
    return _method


@pytest.fixture
def openPwdModal():
    def _method():
        for i in range(5):
            m.click(50, 50, 1)
            time.sleep(fast)
        time.sleep(default)
    return _method


@pytest.fixture
def typeText():
    def _method(symbols):
        for symbol in symbols:
            x = keyboard[symbol][0]
            y = keyboard[symbol][1]
            m.click(x, y, 1)
            time.sleep(fast)
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
