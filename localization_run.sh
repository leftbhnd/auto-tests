#!/bin/bash
TIMEFORMAT="время выполнения тестов локализации: %R"
time {
    pytest -v -m localization_ar_AE --junitxml="/home/promobot/.tests/result/localization_ar_AE.xml"
    sleep 5
    pytest -v -m localization_az_AZ --junitxml="/home/promobot/.tests/result/localization_az_AZ.xml"
    sleep 5
    pytest -v -m localization_cs_CZ --junitxml="/home/promobot/.tests/result/localization_cs_CZ.xml"
    sleep 5
    pytest -v -m localization_de_DE --junitxml="/home/promobot/.tests/result/localization_de_DE.xml"
    sleep 5
    pytest -v -m localization_el_GR --junitxml="/home/promobot/.tests/result/localization_el_GR.xml"
    sleep 5
    pytest -v -m localization_en_US --junitxml="/home/promobot/.tests/result/localization_en_US.xml"
    sleep 5
    pytest -v -m localization_es_ES --junitxml="/home/promobot/.tests/result/localization_es_ES.xml"
    sleep 5
    pytest -v -m localization_fi_FI --junitxml="/home/promobot/.tests/result/localization_fi_FI.xml"
    sleep 5
    pytest -v -m localization_fr_FR --junitxml="/home/promobot/.tests/result/localization_fr_FR.xml"
    sleep 5
    pytest -v -m localization_he_IL --junitxml="/home/promobot/.tests/result/localization_he_IL.xml"
    sleep 5
    pytest -v -m localization_it_IT --junitxml="/home/promobot/.tests/result/localization_it_IT.xml"
    sleep 5
    pytest -v -m localization_nb_NO --junitxml="/home/promobot/.tests/result/localization_nb_NO.xml"
    sleep 5
    pytest -v -m localization_pt_PT --junitxml="/home/promobot/.tests/result/localization_pt_PT.xml"
    sleep 5
    pytest -v -m localization_ro_RO --junitxml="/home/promobot/.tests/result/localization_ro_RO.xml"
    sleep 5
    pytest -v -m localization_ru_RU --junitxml="/home/promobot/.tests/result/localization_ru_RU.xml"
    sleep 5
    pytest -v -m localization_sv_SE --junitxml="/home/promobot/.tests/result/localization_sv_SE.xml"
    sleep 5
    pytest -v -m localization_tr_TR --junitxml="/home/promobot/.tests/result/localization_tr_TR.xml"
    sleep 5
    pytest -v -m localization_uk_UA --junitxml="/home/promobot/.tests/result/localization_uk_UA.xml"
    sleep 5
    pytest -v -m localization_zh_CN --junitxml="/home/promobot/.tests/result/localization_zh_CN.xml"
}