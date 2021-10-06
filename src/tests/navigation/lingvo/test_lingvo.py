#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import slowly
'''
X seconds
'''


@pytest.mark.navigation_lingvo
def test_first_point(node):
    node.autoModePub()
    node.asrPub('едь на первую точку')
    while node.getCurrentPoint() != 1:
        time.sleep(slowly)
    assert node.getAnswer() == 'Приехал на первую точку'


@pytest.mark.navigation_lingvo
def test_second_point(node):
    node.asrPub('едь на вторую точку')
    while node.getCurrentPoint() != 2:
        time.sleep(slowly)
    assert node.getAnswer() == 'Приехал на вторую точку'


@pytest.mark.navigation_lingvo
def test_change_point(node):
    node.asrPub('едь на третью точку')
    while node.getDrivePause() != False:
        time.sleep(slowly)
    time.sleep(5)
    node.asrPub('едь на 1 первую точку')
    assert node.getAnswer() == 'Еду на первую точку'


@pytest.mark.navigation_lingvo
def test_waiting(node):
    while node.getCurrentPoint() != 1:
        time.sleep(slowly)
    time.sleep(60)
    assert node.getCurrentPoint() == 1


@pytest.mark.navigation_lingvo
def test_reset(node):
    node.chargeAppPub()
    time.sleep(60)
    assert node.getChargeState() == True
