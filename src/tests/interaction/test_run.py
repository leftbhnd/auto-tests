#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, running
'''
11.02 seconds
'''


@pytest.mark.interaction_start
def test_run(click):
    click(btn.start.play)
    click(modal.radius.yes)
    time.sleep(running)
