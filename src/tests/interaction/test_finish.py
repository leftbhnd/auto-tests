#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, restart
'''
11.02 seconds
'''


@pytest.mark.tests_interaction_finish
def test_run(openServiceMenu, click):
    openServiceMenu()
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
