#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class RobotModal(enum.Enum):
    # модальное окно ввода пароля
    pwd_close = (896, 178)
    pwd_ok = (823, 310)
    pwd_input = (407, 251)
    # de_DE
    pwd_wrong_input_de = (412, 268)
    pwd_wrong_close_de = (893, 171)
    pwd_wrong_ok_de = (832, 328)
    # el_Gr
    pwd_wrong_input_el = (431, 274)
    pwd_wrong_close_el = (889, 160)
    pwd_wrong_ok_el = (833, 334)
    # модальное окно лога ответов
    ans_log_close = (943, 400)
    ans_log_clear = (810, 399)
    # модальное окно настроек синтеза речи
    speech_settings_close = (896, 351)
    # модальное окно добавления лиц в базу
    add_faces_close = (937, 75)
    add_faces_ok = (644, 711)
    # модальное окно подключения к Wi-Fi
    wifi_pwd_input = (415, 400)
    wifi_pwd_eye = (870, 397)
    wifi_pwd__ok = (809, 444)
    wifi_pwd_close = (889, 319)
    wifi_kb_pwd_input = (407, 264)
    wifi_kb_pwd_ok = (816, 299)
    wifi_kb_pwd_eye = (871, 257)
    wifi_kb_pwd_close = (892, 179)
    # модальное окно сохранения настроек
    save_yes = (818, 441)
    save_no = (651, 441)
    save_close = (890, 339)
    # модальное окно перезапуска интерфейса
    restart_yes = (830, 461)
    restart_no = (655, 454)
    restart_close = (905, 329)
    # модальное окно радиуса
    radius_yes = (818, 479)
    radius_no = (639, 477)
    radius_close = (889, 300)
    radius_increase = (701, 412)
    radius_decrease = (580, 412)
    # модальное окно отсутствия подключения
    no_connection_yes = (829, 455)
    no_connection_no = (649, 457)
    no_connection_close = (898, 324)
    # модальное окно смены пароля
    ident_pwd_input = (666, 373)
    ident_pwd_eye = (916, 373)
    ident_confirm_input = (657, 418)
    ident_confirm_eye = (917, 413)
    ident_save = (846, 464)
    ident_close = (936, 294)
    ident_close_en = (892, 296)
    ident_close_az = (893, 300)
    ident_close_cs = (888, 294)
    ident_close_de = (955, 291)
    ident_close_el = (1057, 292)
    ident_kb_pwd_input = (675, 247)
    ident_kb_pwd_eye = (919, 248)
    ident_kb_confirm_input = (666, 287)
    ident_kb_confirm_input_eye = (922, 285)
    ident_kb_save = (824, 324)
    ident_kb_close = (937, 148)
    # модальное окно инфо о подключении
    connection_info_close = (889, 308)
    # модальное окно раздела промо
    promo_close = (909, 194)
    promo_no = (661, 583)
    promo_yes = (833, 589)
