#!/bin/bash
TIMEFORMAT="время выполнения тестов интерфейса: %R"
time {
    pytest -v -m interface_apps_menu --junitxml="/home/promobot/.tests/result/interface_apps_menu.xml"
    sleep 5
    pytest -v -m interface_dialog_line --junitxml="/home/promobot/.tests/result/interface_dialog_line.xml"
    sleep 5
    pytest -v -m interface_identification --junitxml="/home/promobot/.tests/result/interface_identification.xml"
    sleep 5
    pytest -v -m interface_promo_printing --junitxml="/home/promobot/.tests/result/interface_promo_printing.xml"
    sleep 5
    pytest -v -m interface_promo_slideshow --junitxml="/home/promobot/.tests/result/interface_promo_slideshow.xml"
    sleep 5
    pytest -v -m interface_quick_access --junitxml="/home/promobot/.tests/result/interface_quick_access.xml"
    sleep 5
    pytest -v -m interface_statuses_of_running --junitxml="/home/promobot/.tests/result/interface_statuses_of_running.xml"
    sleep 5
    pytest -v -m interface_testing --junitxml="/home/promobot/.tests/result/interface_testing.xml"
    sleep 5
    pytest -v -m interface_wifi_input --junitxml="/home/promobot/.tests/result/interface_wifi_input.xml"
}