#!/usr/bin/env python
# -*- coding: utf-8 -*-

kb_symbols_dict = {
    # letters
    'й': (429, 725), 'ц': (518, 725), 'у': (618, 725), 'к': (710, 725),
    'е': (810, 725), 'н': (906, 725), 'г': (1008, 725), 'ш': (1093, 725),
    'щ': (1194, 725), 'з': (1293, 725), 'х': (1394, 725),
    'ф': (441, 825), 'ы': (532, 825), 'в': (618, 825),
    'а': (714, 825), 'п': (813, 825), 'р': (820, 825), 'о': (985, 825),
    'л': (1086, 825), 'д': (1165, 825), 'ж': (1256, 825), "э": (1354, 825),
    'я': (510, 925), 'ч': (606, 925), 'с': (700, 925), 'м': (796, 925),
    'и': (885, 925), 'т': (978, 925), 'ь': (1074, 925), 'б': (1160, 925),
    'ю': (1158, 925),
    # numbers
    '1': (285, 565), '2': (358, 565), '3': (425, 565),
    '4': (502, 565), '5': (574, 565), '6': (641, 565), '7': (712, 565),
    '8': (781, 565), '9': (856, 565), '0': (925, 565)
}


buttons_dict = {
    # модалка пароля
    'pass_modal_close': (896, 178), 'pass_modal_ok': (823, 310), 'pass_modal_input': (407, 251),
    # модалка подключения к Wi-Fi
    'wifi_pass_modal_input': (415, 400), 'wifi_pass_modal_eye': (870, 397),
    'wifi_pass_modal_ok': (809, 444), 'wifi_pass_modal_close': (889, 319),
    'kb_wifi_pass_modal_input': (407, 264), 'kb_wifi_pass_modal_ok': (816, 299),
    'kb_wifi_pass_modal_eye': (871, 257), 'kb_wifi_pass_modal_close': (892, 179),
    # модалка сохранения настроек
    'save_modal_yes': (818, 441), 'save_modal_no': (651, 441),
    'save_modal_close': (890, 339),
    # модалка перезапуска интерфейса
    'restart_modal_yes': (830, 461), 'restart_modal_no': (655, 454),
    'restart_modal_close': (905, 329),
    # модалка радиуса движения
    'radius_modal_yes': (818, 479), 'radius_modal_no': (639, 477),
    'radius_modal_close': (889, 300), 'radius_modal_increase': (701, 412),
    'radius_modal_decrease': (580, 412),
    # модалка отсутствия подключения
    'no_connection_modal_yes': (829, 455), 'no_connection_modal_no': (649, 457),
    'no_connection_modal_close': (898, 324),
    # модалка смены пароля
    'ident_modal_pass_input': (666, 373), 'kb_ident_modal_pass_input': (675, 247),
    'ident_modal_pass_eye': (916, 373), 'kb_ident_modal_pass_eye': (919, 248),
    'ident_modal_confirm_input': (657, 418), 'kb_ident_modal_confirm_input': (666, 287),
    'ident_modal_confirm_eye': (917, 413), 'kb_ident_modal_confirm_input_eye': (922, 285),
    'ident_modal_save': (846, 464), 'kb_ident_modal_save': (824, 324),
    'ident_modal_close': (936, 294), 'kb_ident_modal_close': (937, 148),
    # модалка инфо о подключении
    'connection_info_modal_close': (889, 308),
    # модалка раздела "Промо"
    'promo_modal_close': (909, 194), 'promo_modal_no': (661, 583),
    'promo_modal_yes': (833, 589),
    # кнопки стартового экрана
    'control': (617, 671), 'choose_numbers': (299, 758), 'delete': (996, 563), 'play': (635, 413),
    # кнопки раздела "Управление"
    'connection': (206, 195), 'promo': (205, 279), 'testing': (206, 366),
    'settings': (190, 443), 'browser': (183, 530), 'browser_close': (1195, 77),
    'identification': (191, 607), 'send_to_charge': (1173, 454),
    'send_to_charge_close': (1237, 73), 'auto_mode': (1169, 507),
    'phrase_mode': (1169, 553), 'answers_log': (1168, 598), 'hide': (1170, 652),
    'restart': (1172, 713), 'arrow_up': (611, 328), 'arrow_up_right': (731, 302),
    'arrow_right': (728, 457), 'arrow_down_right': (729, 600),
    'arrow_down': (608, 570), 'arrow_down_left': (482, 598), 'arrow_left': (488, 453),
    'arrow_up_left': (485, 302),
    # кнопки раздела "Настройки"
    'system': (258, 290), 'applications': (501, 290), 'face_recognize': (754, 297),
    'navigation': (1008, 288), 'lingvo': (265, 574), 'language_settings': (506, 593),
    'internet_services': (759, 587), 'update': (1025, 574),
    # кнопки раздела "Промо"
    'promo_pictures': (735, 239), 'promo_videos': (726, 291), 'promo_add': (535, 682),
    'promo_delete': (744, 681), 'promo_timeout_increase': (309, 733),
    'promo_timeout_decrease': (190, 728), 'promo_selector': (228, 169),
    'promo_choose_print': (193, 240), 'promo_choose_slideshow': (237, 144),
    'fs_promo_choose_all': (1150, 173), 'promo_back_parrent_dir': (697, 242),
    'fs_promo_checkbox1': (680, 305), 'fs_promo_checkbox2': (683, 365),
    'fs_promo_checkbox3': (683, 421), 'fs_promo_checkbox4': (674, 475),
    'fs_promo_checkbox5': (672, 537), 'fs_promo_checkbox6': (675, 598),
    'fs_promo_slider_top': (1201, 237), 'fs_promo_slider_btm': (1204, 632),
    'robot_promo_checkbox1': (86, 249), 'robot_promo_checkbox2': (87, 296),
    'robot_promo_checkbox3': (76, 354), 'robot_promo_checkbox4': (76, 412),
    'robot_promo_checkbox5': (77, 478), 'robot_promo_checkbox6': (80, 535),
    'robot_promo_checkbox7': (88, 590), 'robot_promo_checkbox8': (80, 644),
    'robot_promo_slider_top': (608, 240), 'robot_promo_slider_btm': (610, 632),
    'robot_promo_choose_all': (557, 173),
    # кнопки раздела "Тестирование"
    'test_rotate_head': (190, 234), 'test_hand_right': (180, 378),
    'test_hand_left': (194, 307), 'zero_all_servos': (199, 454),
    'testing_main_camera': (499, 228), 'testing_face_recognize': (508, 315),
    'testing_bottom_camera': (496, 375), 'testing_fisheye_camera': (501, 451),
    'testing_videostream_close': (1210, 66), 'periphery_statuses': (781, 233),
    'testing_record_sound': (1061, 232), 'testing_speech_recognize': (1072, 387),
    'periphery_statuses_close': (1130, 271),
    # кнопки раздела "Настройки"
    'system_hardware': (147, 239), 'system_led': (109, 289),
    'system_dialog': (124, 344), 'system_interaction': (144, 400),
    'system_menu_panel': (148, 460), 'system_mic_array': (132, 518),
    'system_reset': (60, 584), 'applications_main': (198, 193),
    'applications_apps': (160, 241), 'applications_widgets': (150, 297),
    'fr_settings': (157, 190), 'fr_tacker': (113, 237),
    'fr_facedb': (108, 297), 'nav_settings': (174, 194), 'nav_navigation': (152, 242),
    'lingvo_answers': (141, 197), 'lingvo_sources': (129, 239),
    'language_settings_choose': (135, 188), 'language_settings_synthesis': (150, 246),
    'interner_services_post': (155, 185), 'internet_services_sip': (160, 241),
    'internet_services_ya_disk': (184, 301),
    # кнопки настроек раздела "Навигация"
    'useRadius': (1016, 205),
    # кнопки переходов/смены состояний
    'back': (97, 91), 'reset_input': (612, 62),
    # кнопки раздела "Подключение"
    'connection_info': (795, 731), 'connection_update': (359, 729),
    'random_wifi': (437, 234),
    # кнопки запущенной GUI
    'apps_menu_open': (95, 646), 'apps_menu_close': (101, 107),
    # ubuntu
    'activities': (33, 13), 'work_space': (1263, 152)
}
