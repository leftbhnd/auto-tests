#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import time
import pyautogui
import rospy

from PIL import Image, ImageChops
from pymouse import PyMouse
from main import AutoTest
from helpers.helpers import letters_dict, element_dict, screens_dir
from helpers.messages import JoyCmdMsg

timeout = 0.5

m = PyMouse()


@pytest.fixture
def mouseClick():
    def _method(msg):
        m.click(msg.x, msg.y, 1)
        time.sleep(timeout)
    return _method


@pytest.fixture
def screenDiffChecker():
    def _method(original_image):
        pyautogui.screenshot(
            screens_dir + 'screen.png', region=(0, 40, 1280, 800)
        )
        current = Image.open(screens_dir + 'screen.png')
        original = Image.open(
            screens_dir + original_image
        )
        difference = ImageChops.difference(current, original).getbbox()
        return difference
    return _method


@pytest.fixture
def customScreenDiffChecker():
    def _method(image_info):
        left = image_info['coordinates'][0]
        top = image_info['coordinates'][1]
        right = image_info['coordinates'][2]
        bottom = image_info['coordinates'][3]
        pyautogui.screenshot(
            screens_dir + 'screen.png', region=(left, top, right, bottom)
        )
        current = Image.open(screens_dir + 'screen.png')
        original = Image.open(
            screens_dir + image_info['image']
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
        time.sleep(timeout)
        m.release(finishX, finishY, 1)
        time.sleep(timeout)
    return _method


@pytest.fixture
def clickOn():
    def _method(element):
        x = element_dict[element][0]
        y = element_dict[element][1]
        m.click(x, y, 1)
        time.sleep(timeout)
    return _method


@pytest.fixture
def openPasswordModal():
    def _method():
        m.click(50, 50, 1)
        time.sleep(0.1)
        m.click(50, 50, 1)
        time.sleep(0.1)
        m.click(50, 50, 1)
        time.sleep(0.1)
        m.click(50, 50, 1)
        time.sleep(0.1)
        m.click(50, 50, 1)
        time.sleep(timeout)
    return _method


@pytest.fixture
def typeText():
    def _method(array_of_letters):
        for letter in array_of_letters:
            x = letters_dict[letter][0]
            y = letters_dict[letter][1]
            m.click(x, y, 1)
            time.sleep(0.1)
    return _method


@pytest.fixture
def node():
    def _method()
        rospy.init_node('autotest')
        node = AutoTest()
        time.sleep(timeout)
    return _method


@pytest.fixture
def joy():
    joy = JoyCmdMsg()
    return joy
