#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly, interaction
'''
X seconds
'''


@pytest.mark.navigation_lingvo_bmp
def test_first_point(node):
    node.autoModePub()
    node.asrPub('едь на первую точку')
    while node.getCurrentPoint() != 1:
        time.sleep(slowly)
    assert node.getAnswer() == 'Приехал на первую точку'


@pytest.mark.navigation_lingvo_bmp
def test_start_bmp(node):
    time.sleep(interaction)
    assert node.getAnswer() == 'Еду на первую точку'


@pytest.mark.navigation_lingvo_bmp
def test_finish_bmp(node):
    while node.getCurrentPoint() != 1:
        time.sleep(slowly)
    assert node.getAnswer() == 'Приехал на первую точку'


@pytest.mark.navigation_lingvo_bmp
def test_change_point(node):
    node.asrPub('едь на третью точку')
    while node.getDrivePause() != False:
        time.sleep(slowly)
    time.sleep(5)
    node.asrPub('нет')
    assert node.getAnswer() == 'тестовое правило с нет'


@pytest.mark.navigation_lingvo_bmp
def test_waiting_start_bmp(node):
    time.sleep(interaction)
    while node.getDrivePause() != False:
        time.sleep(slowly)
    assert node.getAnswer() == 'Еду на первую точку'


@pytest.mark.navigation_lingvo_bmp
def test_waiting_finish_bmp(node):
    while node.getCurrentPoint() != 1:
        time.sleep(slowly)
    assert node.getAnswer() == 'Приехал на первую точку'


@pytest.mark.navigation_lingvo_bmp
def test_reset(node):
    node.chargeAppPub()
    time.sleep(60)
    assert node.getChargeState() == True
