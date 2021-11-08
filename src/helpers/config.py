#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.helpers.robot_buttons import robot_buttons
from src.helpers.savelovsky_buttons import savelovsky_buttons
from src.helpers.robot_modals import robot_modals
from src.helpers.robot_params import robot_params
from keyboard import robot_keyboard


fast = 0.1
slowly = 1
default = 0.5
restart = 45
running = 10
modals = 3
internet = 5
promo = 10
connection = 11
interaction = 15
resetAnchor = 10
case_timeout = 10
case_test_pause = 20
screen_resolution = (0, 40, 1920, 1060)
screens_dir = '/home/promobot/.tests/screens/'
failed_dir = '/home/promobot/.tests/screens/test_failed/'
btn = savelovsky_buttons
modal = robot_modals
param = robot_params
keyboard = robot_keyboard
