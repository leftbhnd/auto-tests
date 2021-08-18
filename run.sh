#!/bin/sh
pytest -v -m interface_apps_menu --maxfail=3
sleep 67
pytest -v -m interface_connection_modals --maxfail=3
sleep 27
pytest -v -m interface_dialog_line --maxfail=3
sleep 65
pytest -v -m interface_identification --maxfail=3
sleep 45
pytest -v -m interface_promo_printing --maxfail=3
sleep 48
pytest -v -m interface_promo_slideshow --maxfail=3
sleep 45
pytest -v -m interface_quick_access --maxfail=3
sleep 59
pytest -v -m interface_settings --maxfail=3
sleep 50
pytest -v -m interface_statuses_of_running --maxfail=3
sleep 270
pytest -v -m interface_testing --maxfail=3
sleep 163
pytest -v -m interface_wifi_input --maxfail=3
sleep 24