#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class RobotButton(enum.Enum):
    # клавиатура TODO попробовать метод для клавы
    choose_numbers = (299, 758)
    change_lang = (401, 767)
    delete = (996, 563)
    # стартовый экран
    control = (617, 671)
    play = (635, 413)
    # управление
    connection = (206, 195)
    promo = (205, 279)
    testing = (206, 366)
    settings = (190, 443)
    browser = (183, 530)
    browser_close = (1195, 77)
    ident = (191, 607)
    charge_app = (1173, 454)
    charge_app_close = (1237, 73)
    auto_mode = (1169, 507)
    phrase_mode = (1169, 553)
    answers_log = (1168, 598)
    hide = (1170, 652)
    restart = (1172, 713)
    arrow_up = (611, 328)
    arrow_up_right = (731, 302)
    arrow_right = (728, 457)
    arrow_down_right = (729, 600)
    arrow_down = (608, 570)
    arrow_down_left = (482, 598)
    arrow_left = (488, 453)
    arrow_up_left = (485, 302)
    # настройки
    system = (258, 290)
    apps = (501, 290)
    fr = (754, 297)
    nav = (1008, 288)
    lingvo = (265, 574)
    lang_settings = (506, 593)
    internet = (759, 587)
    update = (1025, 574)
    # подключение
    connection_info = (795, 731)
    connection_update = (359, 729)
    connection_choose_wifi = (437, 234)
    # промо
    promo_pictures = (735, 239)
    promo_videos = (726, 291)
    promo_add = (535, 682)
    promo_delete = (744, 681)
    promo_timeout_increase = (309, 733)
    promo_timeout_decrease = (190, 728)
    promo_selector = (228, 169)
    promo_print = (193, 240)
    promo_slideshow = (237, 144)
    promo_parrent_dir = (697, 242)
    promo_fs_choose_all = (1150, 173)
    promo_fs_checkbox1 = (680, 305)
    promo_fs_checkbox2 = (683, 365)
    promo_fs_checkbox3 = (683, 421)
    promo_fs_checkbox4 = (674, 475)
    promo_fs_checkbox5 = (672, 537)
    promo_fs_checkbox6 = (675, 598)
    promo_fs_slider_top = (1201, 237)
    promo_fs_slider_btm = (1204, 632)
    promo_robot_checkbox1 = (86, 249)
    promo_robot_checkbox2 = (87, 296)
    promo_robot_checkbox3 = (76, 354)
    promo_robot_checkbox4 = (76, 412)
    promo_robot_checkbox5 = (77, 478)
    promo_robot_checkbox6 = (80, 535)
    promo_robot_checkbox7 = (88, 590)
    promo_robot_checkbox8 = (80, 644)
    promo_robot_slider_top = (608, 240)
    promo_robot_slider_btm = (610, 632)
    promo_robot_choose_all = (557, 173)
    # тестирование
    test_rotate_head = (190, 234)
    test_hand_right = (180, 378)
    test_hand_left = (194, 307)
    test_zero_all_servos = (199, 454)
    test_main_camera = (499, 228)
    test_fr = (508, 315)
    test_bottom = (496, 375)
    test_fisheye = (501, 451)
    test_videostream_close = (1210, 66)
    test_periphery_statuses = (781, 233)
    test_record_sound = (1061, 232)
    test_speech_recognize = (1072, 387)
    test_periphery_statuses_close = (1130, 271)
    # настройки -> система
    system_hardware = (147, 239)
    system_led = (109, 289)
    system_dialog = (124, 344)
    system_interaction = (144, 400)
    system_menu_panel = (148, 460)
    system_mic_array = (132, 518)
    system_reset = (60, 584)
    system_interaction_down_arrow = (1198, 720)
    system_dialog_down_arrow = (1200, 722)
    # настройки -> приложения
    apps_main = (198, 193)
    apps_applications = (160, 241)
    apps_widgets = (150, 297)
    # настройки -> распознавание лиц
    fr_settings = (157, 190)
    fr_tacker = (113, 237)
    fr_facedb = (108, 297)
    fr_facedb_select_folder = (1070, 401)
    # настройки -> навигация
    nav_settings = (174, 194)
    nav_navigation = (152, 242)
    # настройки -> лингвобаза
    lingvo_answers = (141, 197)
    lingvo_sources = (129, 239)
    lingvo_first_level = (446, 233)
    # настройки -> языковые настройки
    lang_settings_choose = (135, 188)
    lang_settings_synthesis = (150, 246)
    lang_set_default = (439, 353)
    lang_add_lang = (455, 256)
    lang_delete_lang = (458, 302)
    lang_up_arrow = (685, 400)
    lang_down_arrow = (685, 713)
    # первая группа языков
    lang_ar_AE = (465, 411)
    lang_az_AZ = (453, 464)
    lang_cz_CZ = (459, 528)
    lang_de_DE = (472, 579)
    lang_el_GR = (467, 635)
    lang_en_US = (470, 700)
    # вторая группа языков
    lang_es_ES = (465, 411)
    lang_fi_FI = (453, 464)
    lang_fr_FR = (459, 528)
    lang_he_IL = (472, 579)
    lang_it_IT = (467, 635)
    lang_nb_NO = (470, 700)
    # третья группа языков
    lang_pt_PT = (465, 411)
    lang_ro_RO = (453, 464)
    lang_ru_RU = (459, 528)
    lang_sv_SE = (472, 579)
    lang_tr_TR = (467, 635)
    lang_uk_UA = (470, 700)
    # четвартая группа языков
    lang_zn_CN = (470, 700)
    # настройки -> интернет службы
    internet_email = (155, 185)
    internet_sip = (160, 241)
    internet_ya_disk = (184, 301)
    # управление гуи
    back = (97, 91)
    reset_input = (612, 62)
    # запущенная гуи
    apps_menu_open = (95, 646)
    apps_menu_close = (101, 107)
    speech_settings = (1193, 659)
    take_photo = (643, 659)
    print_photo = (1127, 659)
    # ubuntu
    activities = (33, 13)
    work_space = (1263, 152)
    '''
    кастомные кнопки языков
    '''
    # el_GR
    test_hand_right_el = (185, 377)
    system_reset_el = (136, 555)
    # fi_FI
    connection_info_fi = (864, 730)
    connection_update_fi = (330, 726)
    test_main_camera_fi = (482, 226)
    test_fr_fi = (469, 282)
    test_bottom_fi = (466, 349)
    test_fisheye_fi = (470, 397)
    test_record_sound_fi = (1151, 222)
    system_reset_fi = (119, 552)
    # it_IT
    system_reset_it = (125, 552)
    # nb_NO
    system_reset_nb = (124, 555)
    # sv_SE
    test_periphery_statuses_sv = (903, 219)
    # uk_UA
    test_hand_right_uk = (147, 322)
    test_main_camera_uk = (453, 225)
    test_fr_uk = (433, 273)
    test_bottom_uk = (444, 319)
    test_fisheye_uk = (448, 370)
    system_reset_uk = (143, 553)
    # zn_CN
    ident_zn = (157, 650)
    connection_info_zn = (912, 726)
    connection_update_zn = (337, 731)
    test_hand_right_zn = (174, 344)
    test_main_camera_zn = (482, 232)
    test_fr_zn = (483, 291)
    test_bottom_zn = (494, 346)
    test_fisheye_zn = (475, 405)
    test_main_camera_zn = (482, 232)
    '''
    inverted for ar_AE he_IL
    '''
    # управление
    inv_connection = (1128, 198)
    inv_promo = (1121, 279)
    inv_testing = (1128, 362)
    inv_settings = (1126, 442)
    inv_ident = (1119, 605)
    inv_charge_app = (96, 454)
    inv_charge_app_close = (37, 68)
    inv_auto_mode = (99, 508)
    inv_phrase_mode = (134, 546)
    inv_answers_log = (103, 605)
    inv_restart = (106, 714)
    # тестирование
    inv_test_hand_right = (1080, 360)
    inv_test_hand_right_ae = (1095, 380)
    inv_test_main_camera = (780, 226)
    inv_test_main_camera_ae = (775, 244)
    inv_test_fr = (780, 283)
    inv_test_fr_ae = (778, 310)
    inv_test_bottom = (775, 355)
    inv_test_bottom_ae = (773, 387)
    inv_test_fisheye = (780, 434)
    inv_test_fisheye_ae = (776, 451)
    inv_test_videostream_close = (65, 66)
    inv_test_periphery_statuses = (487, 225)
    inv_test_record_sound = (196, 226)
    inv_test_periphery_statuses_close = (140, 277)
    # настройки
    inv_system = (1008, 288)
    inv_apps = (754, 297)
    inv_fr = (501, 290)
    inv_nav = (258, 290)
    inv_lingvo = (1025, 574)
    inv_lang_settings = (759, 587)
    inv_internet = (508, 571)
    inv_update = (265, 574)
    # подключение
    inv_connection_info = (932, 735)
    inv_connection_update = (661, 728)
    # промо
    inv_promo_pictures = (579, 232)
    inv_promo_add = (702, 681)
    inv_promo_delete = (541, 683)
    inv_promo_selector = (973, 180)
    inv_promo_print = (923, 242)
    inv_promo_fs_checkbox1 = (123, 303)
    inv_promo_robot_checkbox1 = (672, 248)
    # настройки -> система
    inv_system_interaction = (1138, 400)
    inv_system_menu_panel = (1142, 446)
    inv_system_mic_array = (1131, 504)
    inv_system_reset = (1157, 550)
    # настройки -> распознавание лиц
    inv_fr_facedb = (1146, 293)
    inv_fr_facedb_select_folder = (166, 406)
    # настройки -> лингвобаза
    inv_lingvo_sources = (1157, 243)
    # настройки -> языковые настройки
    inv_lang_set_default = (837, 351)
    inv_lang_down_arrow = (594, 714)
    # настройки -> интернет службы
    inv_internet_sip = (1170, 239)
    inv_internet_ya_disk = (1160, 291)
    # вторая группа языков
    inv_lang_it_IT = (801, 636)
    inv_lang_az_AZ = (794, 465)
    # управление гуи
    inv_back = (1186, 98)
    # запущенная гуи
    inv_speech_settings = (86, 659)
