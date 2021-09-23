#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class System(enum.Enum):
    hardware = (147, 239)
    led = (109, 289)
    dialog = (124, 344)
    interaction = (144, 400)
    inv_interaction = (1138, 400)
    menu_panel = (148, 460)
    inv_menu_panel = (1142, 446)
    mic_array = (132, 518)
    inv_mic_array = (1131, 504)
    reset = (60, 584)
    inv_reset = (1157, 550)
    reset_el = (136, 555)
    reset_fi = (119, 5)
    reset_it = (125, 552)
    reset_nb = (124, 555)
    reset_uk = (143, 553)
    interaction_down_arrow = (1198, 720)
    dialog_down_arrow = (1200, 722)
