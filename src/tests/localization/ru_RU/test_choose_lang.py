#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.testConfig import modals_timeout
'''
X seconds
'''

@pytest.mark.localization_choose_ru_RU
def test_connection_open(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText('1234567')
    clickOn('pass_modal_ok')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker('localization/ru_RU/ru_wrong_pass_modal.png') is None