#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class Connection(enum.Enum):
    info = (795, 731)
    info_fi = (864, 730)
    info_zn = (912, 726)
    inv_info = (932, 735)
    update = (359, 729)
    update_fi = (330, 726)
    update_zn = (337, 731)
    inv_update = (661, 728)
    choose_wifi = (437, 234)
