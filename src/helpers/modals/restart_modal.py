#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class RestartModal(enum.Enum):
    yes = (830, 461)
    inv_yes = (457, 459)
    no = (655, 454)
    inv_no = (626, 455)
    close = (905, 329)
    inv_close = (382, 320)
