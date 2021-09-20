#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import running, btn, modal
'''
11.02 seconds
'''


@pytest.mark.interaction_start
def test_run(clickOn):
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
