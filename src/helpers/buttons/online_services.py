#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class Internet(enum.Enum):
    mail = (155, 185)
    sip = (160, 241)
    inv_sip = (1170, 239)
    ya_disk = (184, 301)
    inv_ya_disk = (1160, 291)
