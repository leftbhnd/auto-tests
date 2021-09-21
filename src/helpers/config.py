#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.helpers.button import RobotButton
from src.helpers.modal import RobotModal
from src.helpers.params import RobotParams
from keyboard import robot_keyboard

fast = 0.1
slowly = 1
default = 0.5
restart = 40
running = 10
modals = 3
internet = 5
promo = 10
connection = 10
interaction = 15
resetAnchor = 10
screen_resolution = (0, 40, 1280, 760)
screens_dir = '/home/promobot/.tests/screens/'
failed_dir = '/home/promobot/.tests/screens/test_failed/'
btn = RobotButton
modal = RobotModal
params = RobotParams
keyboard = robot_keyboard
