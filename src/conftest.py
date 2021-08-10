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


@pytest.fixture()
def mouseClick():
    def _method(msg):
        m.click(msg.x, msg.y, 1)
        time.sleep(timeout)
    return _method


@pytest.fixture()
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


@pytest.fixture()
def clickOn():
    def _method(element):
        x = element_dict[element][0]
        y = element_dict[element][1]
        m.click(x, y, 1)
        time.sleep(0.1)
    return _method

@pytest.fixture():
def openPasswordModal():
    def _method():
        m.click(50, 50, 1)
        m.click(50, 50, 1)
        m.click(50, 50, 1)
        m.click(50, 50, 1)
        m.click(50, 50, 1)

@pytest.fixture()
def typeText():
    def _method(array_of_letters):
        for letter in array_of_letters:
            x = letters_dict[letter][0]
            y = letters_dict[letter][1]
            m.click(x, y, 1)
            time.sleep(0.1)
    return _method


@pytest.fixture()
def node():
    rospy.init_node('autotest')
    node = AutoTest()
    time.sleep(timeout)
    return node


@pytest.fixture()
def joy():
    joy = JoyCmdMsg()
    return joy
