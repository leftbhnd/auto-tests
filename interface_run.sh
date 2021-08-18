#!/bin/sh
echo 'start interface_apps_menu'
pytest -v -m interface_apps_menu --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_apps_menu.xml"
sleep 65
echo 'finish interface_apps_menu'
echo 'start interface_connection_modals'
pytest -v -m interface_connection_modals --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_connection_modals.xml"
sleep 27
echo 'finish interface_connection_modals'
echo 'start interface_dialog_line'
pytest -v -m interface_dialog_line --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_dialog_line.xml"
sleep 65
echo 'finish interface_dialog_line'
echo 'start interface_identification'
pytest -v -m interface_identification --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_identification.xml"
sleep 45
echo 'finish interface_identification'
echo 'start interface_promo_printing'
pytest -v -m interface_promo_printing --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_promo_printing.xml"
sleep 48
echo 'finish interface_promo_printing'
echo 'start interface_promo_slideshow'
pytest -v -m interface_promo_slideshow --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_promo_slideshow.xml"
sleep 45
echo 'finish interface_promo_slideshow'
echo 'start interface_quick_access'
pytest -v -m interface_quick_access --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_quick_access.xml"
sleep 59
echo 'finish interface_quick_access'
echo 'start interface_settings'
pytest -v -m interface_settings --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_settings.xml"
sleep 50
echo 'finish interface_settings'
echo 'start interface_statuses_of_running'
pytest -v -m interface_statuses_of_running --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_statuses_of_running.xml"
sleep 270
echo 'finish interface_statuses_of_running'
echo 'start interface_testing'
pytest -v -m interface_testing --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_testing.xml"
sleep 163
echo 'finish interface_testing'
echo 'start interface_wifi_input'
pytest -v -m interface_wifi_input --maxfail=3 --junitxml="/home/promobot/.tests/result/interface_wifi_input.xml"
sleep 24
echo 'finish interface_wifi_input'