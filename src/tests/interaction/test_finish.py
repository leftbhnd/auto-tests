#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, restart
'''
11.02 seconds
'''


@pytest.mark.test_interaction_finish
def test_finish(openServiceMenu, click):
    openServiceMenu()
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
