#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import time
import pyautogui as p
import rospy

from datetime import datetime
from PIL import Image, ImageChops
from main import AutoTest
from helpers.config import screens_dir, failed_dir, fast, default, screen_resolution, keyboard
from helpers.messages import JoyCmdMsg


@pytest.fixture
def screenDiffChecker():
    def _method(original_image, coordinates=screen_resolution):
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
def dNd():
    def _method(start, finish):
        p.leftClick(start[0], start[1], 0.5)
        p.dragTo(finish[0], finish[1], 0.5, button='left')
    return _method


@pytest.fixture
def click():
    def _method(button):
        x = button.value[0]
        y = button.value[1]
        p.leftClick(x, y, _pause=False)
        time.sleep(default)
    return _method


@pytest.fixture
def type():
    def _method(symbols):
        for symbol in symbols:
            x = keyboard[symbol][0]
            y = keyboard[symbol][1]
            p.leftClick(x, y, _pause=False)
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
        p.leftClick(407, 251)
        p.leftClick(299, 758)
        p.leftClick(285, 565, _pause=False)
        p.leftClick(358, 565, _pause=False)
        p.leftClick(425, 565, _pause=False)
        p.leftClick(502, 565, _pause=False)
        p.leftClick(574, 565, _pause=False)
        p.leftClick(641, 565, _pause=False)
        p.leftClick(823, 310)
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
