#!/usr/bin/env python
# -*- coding: utf-8 -*-
from button import RobotButton
from modal import RobotModal
from params import RobotParams
from keyboard import robot_keyboard

fast = 0.1
slowly = 1
default = 0.5
restart = 40
running = 10
modals = 3
screen_resolution = (0, 40, 1280, 760)
screens_dir = '/home/promobot/.tests/screens/'
failed_dir = '/home/promobot/.tests/screens/test_failed/'
btn = RobotButton
modal = RobotModal
params = RobotParams
keyboard = robot_keyboard