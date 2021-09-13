#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class RobotParams(enum.Enum):
    # driving
    useRadius = (1016, 205)
    inv_useRadius = (260, 194)
    # dialog
    timeRecently_increase = (1, 1)
    timeRecently_decrease = (1, 1)
    timeRecentlyUnknown_increase = (1, 2)
    timeRecentlyUnknown_decrease = (1, 2)
