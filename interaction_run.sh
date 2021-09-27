#!/bin/sh
echo 'start interaction test'
pytest -v -m test_interaction_start
sleep 5
echo 'start interaction_anchor'
pytest -v -m interaction_anchor --junitxml="/home/promobot/.tests/result/interaction_anchor.xml"
echo 'finish interaction_anchor'
sleep 5
echo 'start interaction_greeting'
pytest -v -m interaction_greeting --junitxml="/home/promobot/.tests/result/interaction_greeting.xml"
echo 'finish interaction_greeting'
sleep 5
echo 'start interaction_interaction'
pytest -v -m interaction_interaction --junitxml="/home/promobot/.tests/result/interaction_interaction.xml"
echo 'finish interaction_interaction'
sleep 5
echo 'start interaction_internet_answer'
pytest -v -m interaction_internet_answer --junitxml="/home/promobot/.tests/result/interaction_internet_answer.xml"
echo 'finish interaction_internet_answer'
sleep 5
echo 'start interaction_jokes'
pytest -v -m interaction_jokes --junitxml="/home/promobot/.tests/result/interaction_jokes.xml"
echo 'finish interaction_jokes'
sleep 5
echo 'start interaction_joy_phrase'
pytest -v -m interaction_joy_phrase --junitxml="/home/promobot/.tests/result/interaction_joy_phrase.xml"
echo 'finish interaction_joy_phrase'
sleep 5
echo 'start interaction_levels'
pytest -v -m interaction_levels --junitxml="/home/promobot/.tests/result/interaction_levels.xml"
echo 'finish interaction_levels'
sleep 5
echo 'start interaction_macros'
pytest -v -m interaction_macros --junitxml="/home/promobot/.tests/result/interaction_macros.xml"
echo 'finish interaction_macros'
sleep 5
echo 'start interaction_promo'
pytest -v -m interaction_promo --junitxml="/home/promobot/.tests/result/interaction_promo.xml"
echo 'finish interaction_promo'
sleep 5
echo 'start interaction_surprises'
pytest -v -m interaction_surprises --junitxml="/home/promobot/.tests/result/interaction_surprises.xml"
echo 'finish interaction_surprises'
sleep 5
echo 'start interaction_two_rules'
pytest -v -m interaction_two_rules --junitxml="/home/promobot/.tests/result/interaction_two_rules.xml"
echo 'finish interaction_two_rules'
sleep 5
echo 'finish interaction test'
pytest -v -m test_interaction_finish
sleep 5
