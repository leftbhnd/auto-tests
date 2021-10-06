#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, running, restart


@pytest.mark.navigation_setup
def test_setup(click, typeText, db):
    db.updateValue([
        {'name': '/driving/useMap', 'value': True},
        {'name': '/driving/useRadius', 'value': False}
    ])
    click(btn.start.control)
    typeText('123456')
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    click(btn.start.play)
    time.sleep(running)
