#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui as p


def makeScreen(image, coordinates=(0, 40, 1280, 760)):
    p.screenshot(
        '/home/promobot/.tests/screens/%s.png' % (image), region=coordinates
    )


def getTuple(left, top, right, bottom):
    return (left, top, right, bottom)


screen_name = raw_input('название скриншота: ')
default = raw_input('задать координаты? 0 - пропустить (дефолт), 1 - задать: ')

if default == '1':
    left = raw_input('отступ слева: ')
    top = raw_input('отступ сверху: ')
    right = raw_input('ширина: ')
    bottom = raw_input('высота: ')
    makeScreen(screen_name, getTuple(left, top, right, bottom))
else:
    makeScreen(screen_name)
