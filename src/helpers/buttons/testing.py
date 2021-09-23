#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class Testing(enum.Enum):
    rotate_head = (190, 234)
    hand_right = (180, 378)
    hand_right_el = (185, 377)
    hand_right_uk = (147, 322)
    hand_right_zn = (174, 344)
    inv_hand_right_ae = (1095, 380)
    inv_hand_right_he = (1080, 360)
    hand_left = (194, 307)
    zero_all_servos = (199, 454)
    main_camera = (499, 228)
    main_camera_fi = (482, 226)
    main_camera_uk = (453, 225)
    main_camera_zn = (482, 232)
    inv_main_camera_ae = (775, 244)
    inv_main_camera_he = (780, 226)
    fr = (508, 315)
    fr_fi = (469, 282)
    fr_uk = (433, 273)
    fr_zn = (483, 291)
    inv_fr_ae = (778, 310)
    inv_fr_he = (780, 283)
    bottom = (496, 375)
    bottom_uk = (444, 319)
    bottom_fi = (466, 349)
    bottom_zn = (494, 346)
    inv_bottom_he = (775, 355)
    inv_bottom_ae = (773, 387)
    fisheye = (501, 451)
    fisheye_fi = (470, 397)
    fisheye_uk = (448, 370)
    fisheye_zn = (475, 405)
    inv_fisheye_ae = (776, 451)
    inv_fisheye_he = (780, 434)
    periphery_statuses = (781, 233)
    periphery_statuses_sv = (903, 219)
    inv_periphery_statuses = (487, 225)
    record = (1061, 232)
    record_fi = (1151, 222)
    inv_record = (196, 226)
    speech_recognize = (1072, 387)