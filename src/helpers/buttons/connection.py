#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class Connection(enum.Enum):
    info = (795, 731)
    info_ae = (932, 735)
    info_fi = (864, 730)
    info_he = (932, 735)
    info_zn = (912, 726)
    update = (359, 729)
    update_ae = (661, 728)
    update_fi = (330, 726)
    update_he = (661, 728)
    update_zn = (337, 731)
    choose_wifi = (437, 234)
