#!/bin/sh
echo 'start interface_apps_menu'
pytest -v -m interface_apps_menu --junitxml="/home/promobot/.tests/result/interface_apps_menu.xml"
sleep 5
echo 'finish interface_apps_menu'
echo 'start interface_dialog_line'
pytest -v -m interface_dialog_line --junitxml="/home/promobot/.tests/result/interface_dialog_line.xml"
sleep 5
echo 'finish interface_dialog_line'
echo 'start interface_identification'
pytest -v -m interface_identification --junitxml="/home/promobot/.tests/result/interface_identification.xml"
sleep 5
echo 'finish interface_identification'
echo 'start interface_promo_printing'
pytest -v -m interface_promo_printing --junitxml="/home/promobot/.tests/result/interface_promo_printing.xml"
sleep 5
echo 'finish interface_promo_printing'
echo 'start interface_promo_slideshow'
pytest -v -m interface_promo_slideshow --junitxml="/home/promobot/.tests/result/interface_promo_slideshow.xml"
sleep 5
echo 'finish interface_promo_slideshow'
echo 'start interface_quick_access'
pytest -v -m interface_quick_access --junitxml="/home/promobot/.tests/result/interface_quick_access.xml"
sleep 5
echo 'finish interface_quick_access'
echo 'start interface_statuses_of_running'
pytest -v -m interface_statuses_of_running --junitxml="/home/promobot/.tests/result/interface_statuses_of_running.xml"
sleep 5
echo 'finish interface_statuses_of_running'
echo 'start interface_testing'
pytest -v -m interface_testing --junitxml="/home/promobot/.tests/result/interface_testing.xml"
sleep 5
echo 'finish interface_testing'
echo 'start interface_wifi_input'
pytest -v -m interface_wifi_input --junitxml="/home/promobot/.tests/result/interface_wifi_input.xml"
sleep 5
echo 'finish interface_wifi_input'