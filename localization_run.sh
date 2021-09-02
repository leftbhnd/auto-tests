#!/bin/sh
echo 'start localization_ru_RU'
pytest -v -m localization_ru_RU --junitxml="/home/promobot/.tests/result/localization_ru_RU.xml"
sleep 65
echo 'finish localization_ru_RU'