#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class System(enum.Enum):
    hardware = (147, 239)
    hardware_ae = (1179, 241)
    hardware_he = (1179, 241)
    led = (109, 289)
    led_ae = (1181, 287)
    led_he = (1181, 287)
    dialog = (124, 344)
    dialog_ae = (1185, 344)
    dialog_he = (1185, 344)
    interaction = (144, 400)
    interaction_ae = (1138, 400)
    interaction_he = (1138, 400)
    menu_panel = (148, 460)
    menu_panel_ae = (1142, 446)
    menu_panel_he = (1142, 446)
    mic_array = (132, 518)
    mic_array_ae = (1131, 504)
    mic_array_he = (1131, 504)
    reset = (60, 584)
    reset_ae = (1157, 550)
    reset_el = (136, 555)
    reset_fi = (119, 554)
    reset_he = (1157, 550)
    reset_it = (125, 552)
    reset_nb = (124, 555)
    reset_uk = (143, 553)
