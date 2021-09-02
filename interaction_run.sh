#!/bin/sh
echo 'start interaction'
pytest -v -m interaction_start
sleep 15
echo 'start interaction_joystick_phrase'
pytest -v -m interaction_joy_phrase --junitxml="/home/promobot/.tests/result/interaction_joy_phrase.xml"
sleep X
echo 'finish interaction_joystick_phrase'
echo 'start interaction_promo_setup'
pytest -v -m interaction_promo_setup
sleep X
echo 'finish interaction_promo_setup'
echo 'start interaction_promo'
pytest -v -m interaction_promo --junitxml="/home/promobot/.tests/result/interaction_promo.xml"
sleep X
echo 'finish interaction_promo'