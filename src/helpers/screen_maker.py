#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui

screen_name = raw_input('название скриншота: ')
pyautogui.screenshot(
    '/home/promobot/Documents/%s.png' % (screen_name), region=(0, 40, 1280, 800)
)
