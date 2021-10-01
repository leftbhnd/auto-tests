#!/bin/bash
TIMEFORMAT="время выполнения тестов взаимодействия: %R"
time {
    pytest -v -m test_interaction_start
    sleep 5
    pytest -v -m interaction_anchor --junitxml="/home/promobot/.tests/result/interaction_anchor.xml"
    sleep 5
    pytest -v -m interaction_greeting --junitxml="/home/promobot/.tests/result/interaction_greeting.xml"
    sleep 5
    pytest -v -m interaction_interaction --junitxml="/home/promobot/.tests/result/interaction_interaction.xml"
    sleep 5
    pytest -v -m interaction_internet_answer --junitxml="/home/promobot/.tests/result/interaction_internet_answer.xml"
    sleep 5
    pytest -v -m interaction_jokes --junitxml="/home/promobot/.tests/result/interaction_jokes.xml"
    sleep 5
    pytest -v -m interaction_joy_phrase --junitxml="/home/promobot/.tests/result/interaction_joy_phrase.xml"
    sleep 5
    pytest -v -m interaction_levels --junitxml="/home/promobot/.tests/result/interaction_levels.xml"
    sleep 5
    pytest -v -m interaction_macros --junitxml="/home/promobot/.tests/result/interaction_macros.xml"
    sleep 5
    pytest -v -m interaction_promo --junitxml="/home/promobot/.tests/result/interaction_promo.xml"
    sleep 5
    pytest -v -m interaction_surprises --junitxml="/home/promobot/.tests/result/interaction_surprises.xml"
    sleep 5
    pytest -v -m interaction_two_rules --junitxml="/home/promobot/.tests/result/interaction_two_rules.xml"
    sleep 5
    pytest -v -m test_interaction_finish
}