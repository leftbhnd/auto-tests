#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid


class AsrTtsMsg:
    def __init__(self, text):
        self.text = text
        self.uuid = str(uuid.uuid4())


class SwipeMsg:
    def __init__(self, start, finish):
        # 2 кортежа, нажатие -> сдвиг
        self.startX = start[0]
        self.startY = start[1]
        self.finishX = finish[0]
        self.finishY = finish[1]


class JoyCmdMsg:
    def __init__(self):
        '''
        axes = [0.0, 0.0, 0.0, 0.0, RT, LT]
        buttons = [A, B, 0, X, Y, 0, LB, RB, 0, 0, 0, start, 0, 0, 0, back, 0, up, right, down, left]
        '''
        self._axes = [0.0, 0.0, 0.0, 0.0, 1.0, 1.0]
        self._buttons = [
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]

    def upVolume(self):
        # X LB
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[3], first_press_buttons[6] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[3], second_press_buttons[6] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def downVolume(self):
        # X LT
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[3], first_press_axes[5] = 1, -1.0

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[3], second_press_axes[5] = 1, 1.0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def upMic(self):
        # X RB
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[3], first_press_buttons[7] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[3], second_press_buttons[7] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def downMic(self):
        # X RT
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[3], first_press_axes[4] = 1, -1.0

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[3], second_press_axes[4] = 1, 1.0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def phraseMode(self):
        # back Y
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[15], first_press_buttons[4] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[15], second_press_buttons[4] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def nextPhrase(self):
        # Y RT
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[4], first_press_axes[4] = 1, -1.0

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[4], second_press_axes[4] = 1, 1.0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def previousPhrase(self):
        # Y RB
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[4], first_press_buttons[7] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[4], second_press_buttons[7] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def autoMode(self):
        # back start
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[15], first_press_buttons[11] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[15], second_press_buttons[11] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]
