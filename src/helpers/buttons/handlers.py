#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class Handlers(enum.Enum):
    back = (97, 91)
    back_ae = (1186, 98)
    back_he = (1186, 98)
    reset = (612, 62)
    lang_up_arr = (685, 400)
    lang_down_arr = (685, 713)
    lang_down_arr_ae = (594, 714)
    lang_down_arr_he = (594, 714)
    interaction_down_arr = (1198, 720)
    dialog_down_arr = (1200, 722)
