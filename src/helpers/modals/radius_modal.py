#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class RadiusModal(enum.Enum):
    yes = (818, 479)
    inv_yes = (451, 467)
    no = (639, 477)
    close = (889, 300)
    increase = (701, 412)
    decrease = (580, 412)
