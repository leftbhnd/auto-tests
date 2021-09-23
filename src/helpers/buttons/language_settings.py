#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum


class LanguageSettings(enum.Enum):
    set_lang = (135, 188)
    synthesis = (150, 246)
    set_default = (439, 353)
    inv_set_default = (837, 351)
    add_lang = (455, 256)
    delete_lang = (458, 302)
    up_arrow = (685, 400)
    down_arrow = (685, 713)
    inv_down_arrow = (594, 714)
    # первая группа языков
    ar_AE = (465, 411)
    az_AZ = (453, 464)
    az_AZ = (794, 465)
    cz_CZ = (459, 528)
    de_DE = (472, 579)
    el_GR = (467, 635)
    en_US = (470, 700)
    # вторая группа языков
    es_ES = (465, 411)
    fi_FI = (453, 464)
    fr_FR = (459, 528)
    he_IL = (472, 579)
    it_IT = (467, 635)
    inv_it_IT = (801, 636)
    nb_NO = (470, 700)
    # третья группа языков
    pt_PT = (465, 411)
    ro_RO = (453, 464)
    ru_RU = (459, 528)
    sv_SE = (472, 579)
    tr_TR = (467, 635)
    uk_UA = (470, 700)
    # четвартая группа языков
    zn_CN = (470, 700)
