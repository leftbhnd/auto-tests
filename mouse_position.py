#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymouse import PyMouse

m = PyMouse()
result = []

def getter():
    point_name = ''
    while True:
        point_name = raw_input('название координаты: ')
        coordinates = m.position()
        result.append([coordinates, point_name])
        print(result)

getter()