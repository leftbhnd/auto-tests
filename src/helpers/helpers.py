#!/usr/bin/env python
# -*- coding: utf-8 -*-

letters_dict = {'й': (429, 725), 'ц': (518, 725), 'у': (618, 725), 'к': (710, 725),
                'е': (810, 725), 'н': (906, 725), 'г': (1008, 725), 'ш': (1093, 725),
                'щ': (1194, 725), 'з': (1293, 725), 'х': (1394, 725),
                'delete': (1500, 725), 'ф': (441, 825), 'ы': (532, 825), 'в': (618, 825),
                'а': (714, 825), 'п': (813, 825), 'р': (820, 825), 'о': (985, 825),
                'л': (1086, 825), 'д': (1165, 825), 'ж': (1256, 825), "э": (1354, 825),
                'я': (510, 925), 'ч': (606, 925), 'с': (700, 925), 'м': (796, 925),
                'и': (885, 925), 'т': (978, 925), 'ь': (1074, 925), 'б': (1160, 925),
                'ю': (1158, 925), '1': (285, 565), '2': (358, 565), '3': (425, 565),
                '4': (502, 565), '5': (574, 565), '6': (641, 565), '7': (712, 565),
                '8': (781, 565), '9': (856, 565), '0': (925, 565)
                }


element_dict = {
    # модалки
    'pass_modal_close': (896, 178), 'pass_modal_ok': (823, 310), 'pass_modal_input': (407, 251),
    'save_modal_yes': (818, 441), 'save_modal_no': (651, 441),
    'save_modal_close': (890, 339), 'restart_modal_yes': (830, 461),
    'restart_modal_no': (655, 454), 'restart_modal_close': (905, 329),
    'radius_modal_yes': (818, 479), 'radius_modal_no': (639, 477),
    'radius_modal_close': (889, 300), 'radius_modal_increase': (701, 412),
    'radius_modal_decrease': (580, 412), 'no_connection_modal_yes': (829, 455),
    'no_connection_modal_no': (649, 457), 'no_connection_modal_close': (898, 324),
    'ident_modal_pass_input': (666, 373), 'ident_modal_pass_eye': (916, 373),
    'ident_modal_confirm_input': (657, 418), 'ident_modal_confirm_eye': (917, 413),
    'ident_modal_save': (846, 464), 'ident_modal_close': (936, 294),
    # кнопки
    'control': (617, 671), 'choose_numbers': (299, 758), 'connection': (206, 195),
    'promo': (205, 279), 'testing': (206, 366), 'settings': (190, 443),
    'browser': (183, 530), 'browser_close': (1195, 77), 'identification': (191, 607),
    'send_to_charge': (1173, 454), 'send_to_charge_close': (1237, 73),
    'auto_mode': (1169, 507), 'phrase_mode': (1169, 553), 'answers_log': (1168, 598),
    'hide': (1170, 652), 'restart': (1172, 713), 'arrow_up': (611, 328),
    'arrow_up_right': (731, 302), 'arrow_right': (728, 457), 'arrow_down_right': (729, 600),
    'arrow_down': (608, 570), 'arrow_down_left': (482, 598), 'arrow_left': (488, 453),
    'arrow_up_left': (485, 302), 'system': (258, 290), 'applications': (501, 290),
    'face_recognize': (754, 297), 'navigation': (1008, 288), 'lingvo': (265, 574),
    'language_settings': (506, 593), 'internet_services': (759, 587), 'update': (1025, 574),
    'back': (97, 91), 'play': (635, 413), 'useRadius': (1016, 205), 'apps_menu_open': (95, 646),
    'apps_menu_close': (101, 107), 'reset_input': (612, 62),
    # ubuntu
    'activities': (33, 13), 'work_space': (1263, 152)
}


screens_dir = '/home/promobot/.tests/screens/'
