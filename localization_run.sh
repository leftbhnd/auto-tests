#!/bin/sh
echo 'start localization_ar_AE'
pytest -v -m localization_ar_AE --junitxml="/home/promobot/.tests/result/localization_ar_AE.xml"
sleep 300
echo 'finish localization_ar_AE'
sleep 5
echo 'start localization_az_AZ'
pytest -v -m localization_az_AZ --junitxml="/home/promobot/.tests/result/localization_az_AZ.xml"
sleep 300
echo 'finish localization_az_AZ'
sleep 5
echo 'start localization_cs_CZ'
pytest -v -m localization_cs_CZ --junitxml="/home/promobot/.tests/result/localization_cs_CZ.xml"
sleep 300
echo 'finish localization_cs_CZ'
sleep 5
echo 'start localization_de_DE'
pytest -v -m localization_de_DE --junitxml="/home/promobot/.tests/result/localization_de_DE.xml"
sleep 300
echo 'finish localization_de_DE'
sleep 5
echo 'start localization_el_GR'
pytest -v -m localization_el_GR --junitxml="/home/promobot/.tests/result/localization_el_GR.xml"
sleep 300
echo 'finish localization_el_GR'
sleep 5
echo 'start localization_en_US'
pytest -v -m localization_en_US --junitxml="/home/promobot/.tests/result/localization_en_US.xml"
sleep 300
echo 'finish localization_en_US'
sleep 5
echo 'start localization_es_ES'
pytest -v -m localization_es_ES --junitxml="/home/promobot/.tests/result/localization_es_ES.xml"
sleep 300
echo 'finish localization_es_ES'
sleep 5
echo 'start localization_fi_FI'
pytest -v -m localization_fi_FI --junitxml="/home/promobot/.tests/result/localization_fi_FI.xml"
sleep 300
echo 'finish localization_fi_FI'
sleep 5
echo 'start localization_fr_FR'
pytest -v -m localization_fr_FR --junitxml="/home/promobot/.tests/result/localization_fr_FR.xml"
sleep 300
echo 'finish localization_fr_FR'
sleep 5
echo 'start localization_he_IL'
pytest -v -m localization_he_IL --junitxml="/home/promobot/.tests/result/localization_he_IL.xml"
sleep 300
echo 'finish localization_he_IL'
sleep 5
echo 'start localization_it_IT'
pytest -v -m localization_it_IT --junitxml="/home/promobot/.tests/result/localization_it_IT.xml"
sleep 300
echo 'finish localization_it_IT'
sleep 5
echo 'start localization_nb_NO'
pytest -v -m localization_nb_NO --junitxml="/home/promobot/.tests/result/localization_nb_NO.xml"
sleep 300
echo 'finish localization_nb_NO'
sleep 5
echo 'start localization_pt_PT'
pytest -v -m localization_pt_PT --junitxml="/home/promobot/.tests/result/localization_pt_PT.xml"
sleep 300
echo 'finish localization_pt_PT'
sleep 5
echo 'start localization_ro_RO'
pytest -v -m localization_ro_RO --junitxml="/home/promobot/.tests/result/localization_ro_RO.xml"
sleep 300
echo 'finish localization_ro_RO'
sleep 5
echo 'start localization_ru_RU'
pytest -v -m localization_ru_RU --junitxml="/home/promobot/.tests/result/localization_ru_RU.xml"
sleep 300
echo 'finish localization_ru_RU'
sleep 5
echo 'start localization_sv_SE'
pytest -v -m localization_sv_SE --junitxml="/home/promobot/.tests/result/localization_sv_SE.xml"
sleep 300
echo 'finish localization_sv_SE'
sleep 5
echo 'start localization_tr_TR'
pytest -v -m localization_tr_TR --junitxml="/home/promobot/.tests/result/localization_tr_TR.xml"
sleep 300
echo 'finish localization_tr_TR'
sleep 5
echo 'start localization_uk_UA'
pytest -v -m localization_uk_UA --junitxml="/home/promobot/.tests/result/localization_uk_UA.xml"
sleep 300
echo 'finish localization_uk_UA'
sleep 5
echo 'start localization_zh_CN'
pytest -v -m localization_zh_CN --junitxml="/home/promobot/.tests/result/localization_zh_CN.xml"
sleep 300
echo 'finish localization_zh_CN'
sleep 5