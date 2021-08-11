#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui

print('введите отступ слева->сверху->справа->снизу')
print('например, для полного скриншота экрана без header это: 0->40->1280->800')
print('для запущенной gui без header и без диалоговой строки это: 0->40->1280->660')

left = raw_input('отступ слева: ')
top = raw_input('отступ сверху: ')
right = raw_input('отступ справа: ')
bottom = raw_input('отступ снизу: ')

screen_name = raw_input('название скриншота: ')
pyautogui.screenshot(
    '/home/promobot/.tests/screens/%s.png' % (screen_name), region=(int(left), int(top), int(right), int(bottom))
)
