#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import time
import rospy

from main import AutoTest
from services.db_request import DbRequest
from services.gui import Gui
from helpers.messages import JoyCmdMsg

@pytest.fixture
def gui():
    gui = Gui()
    return gui


@pytest.fixture
def node():
    rospy.init_node('autotest')
    node = AutoTest()
    time.sleep(default)
    return node


@pytest.fixture
def joy():
    joy = JoyCmdMsg()
    return joy


@pytest.fixture
def db():
    db = DbRequest()
    return db
