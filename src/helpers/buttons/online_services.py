#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class Internet(enum.Enum):
    mail = (155, 185)
    sip = (160, 241)
    sip_ae = (1170, 239)
    sip_he = (1170, 239)
    ya_disk = (184, 301)
    ya_disk_ae = (1160, 291)
    ya_disk_he = (1160, 291)
