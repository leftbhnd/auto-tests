#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class DialogParams(enum.Enum):
    timeRecently_increase = (1117, 700)
    timeRecently_decrease = (893, 700)
    timeRecentlyUnknown_increase = (1117, 650)
    timeRecentlyUnknown_decrease = (895, 650)
