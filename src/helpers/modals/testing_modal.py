#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class TestingModal(enum.Enum):
    periphery_close = (1130, 271)
    videostream_close = (1210, 66)
    inv_videostream_close = (65, 66)
