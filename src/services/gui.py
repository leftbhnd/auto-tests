#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import pyautogui as p

from datetime import datetime
from PIL import Image, ImageChops
from src.helpers.config import screens_dir, failed_dir, default, screen_resolution, keyboard


class Gui:
    def screenDiffChecker(original_image, coordinates):
        p.screenshot(
            screens_dir + 'screen.png', region=coordinates
        )
        current = Image.open(
            screens_dir + 'screen.png'
        )
        try:
            original = Image.open(
                screens_dir + original_image
            )
        except IOError:
            p.screenshot(
                screens_dir + original_image, region=coordinates
            )
            original = Image.open(
                screens_dir + original_image
            )
        result = ImageChops.difference(current, original)
        difference = result.getbbox()
        if difference != None:
            result.save(
                failed_dir + 'failed_' + original_image +
                datetime.now().strftime("%d.%m.%Y.%H:%M:%S") + '.png'
            )
        return difference

    def dNd(start, finish):
        p.leftClick(start[0], start[1], 0.5)
        p.dragTo(finish[0], finish[1], 0.5, button='left')

    def click(button):
        x = button.value[0]
        y = button.value[1]
        p.leftClick(x, y, _pause=False)
        time.sleep(default)

    def raw_click(coords):
        x = coords[0]
        y = coords[1]
        p.leftClick(x, y, _pause=False)
        time.sleep(default)

    def typeText(symbols):
        if type(symbols) != str:
            p.leftClick(299, 758, _pause=False)
            symbols = str(symbols)
        for symbol in symbols:
            x = keyboard[symbol][0]
            y = keyboard[symbol][1]
            p.leftClick(x, y, _pause=False)

    def openPwdModal():
        for i in range(4):
            p.leftClick(50, 50)
        time.sleep(default)

    def openServiceMenu():
        for i in range(4):
            p.leftClick(50, 50)
            p.leftClick(299, 758)
            p.leftClick(285, 565, _pause=False)
            p.leftClick(358, 565, _pause=False)
            p.leftClick(425, 565, _pause=False)
            p.leftClick(502, 565, _pause=False)
            p.leftClick(574, 565, _pause=False)
            p.leftClick(641, 565, _pause=False)
            p.leftClick(823, 310)
