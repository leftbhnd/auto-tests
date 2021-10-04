#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly
'''
X seconds
'''


@pytest.mark.navigation_map_json
def test_first_point_text_start(node):
    node.autoModePub()
    while node.getInteraction() != [False, 100]:
        time.sleep(default)
    assert node.getAnswer() == 'Еду на первую точку'


@pytest.mark.navigation_map_json
def test_first_point_text_finish(node):
    while node.getCurrentPoint() != 1:
        time.sleep(slowly)
    assert node.getAnswer() is 'Приехал на первую точку'


@pytest.mark.navigation_map_json
def test_first_point_action_first(node):
    assert node.getScriptProcess() == [True, 'talk1']


@pytest.mark.navigation_map_json
def test_first_point_action_second(node):
    # таймаут в map.json
    time.sleep(5)
    assert node.getScriptProcess() == [True, 'talk3']


@pytest.mark.navigation_map_json
def test_second_point_text_start(node):
    # таймаут в map.json
    time.sleep(1)
    assert node.getAnswer() == 'Еду на вторую точку'


@pytest.mark.navigation_map_json
def test_second_point_text_finish(node):
    while node.getCurrentPoint() != 2:
        time.sleep(slowly)
    assert node.getAnswer() is 'Приехал на вторую точку точку'


@pytest.mark.navigation_map_json
def test_second_point_action_first(node):
    assert node.getScriptProcess() == [True, 'talk1']


@pytest.mark.navigation_map_json
def test_second_point_action_second(node):
    # таймаут в map.json
    time.sleep(5)
    assert node.getScriptProcess() == [True, 'talk3']


@pytest.mark.navigation_map_json
def test_third_point_text_start(node):
    # таймаут в map.json
    time.sleep(1)
    assert node.getAnswer() == 'Еду на третью точку'


@pytest.mark.navigation_map_json
def test_third_point_text_finish(node):
    while node.getCurrentPoint() != 2:
        time.sleep(slowly)
    assert node.getAnswer() is 'Приехал на третью точку точку'


@pytest.mark.navigation_map_json
def test_third_point_action_first(node):
    assert node.getScriptProcess() == [True, 'talk1']


@pytest.mark.navigation_map_json
def test_third_point_action_second(node):
    # таймаут в map.json
    time.sleep(5)
    assert node.getScriptProcess() == [True, 'talk3']


@pytest.mark.navigation_map_json
def test_back_to_first_point(node):
    # таймаут в map.json
    time.sleep(1)
    assert node.getAnswer() == 'Еду на первую точку'


@pytest.mark.navigation_map_json
def test_restore(node):
    node.chargeAppPub()
    # TODO может обыграть по-другому, например screenDiffChecker
    time.sleep(60)
    assert node.getChargeState() == True
