#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class NoInternetConnection(enum.Enum):
    yes = (829, 455)
    inv_yes = (454, 455)
    no = (649, 457)
    close = (898, 324)
