#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, running, restart


@pytest.mark.navigation_restore
def test_restore(click, typeText, db):
    db.updateValue([
        {'name': '/driving/useMap', 'value': False},
        {'name': '/driving/useRadius', 'value': True}
    ])
    click(btn.start.control)
    typeText('123456')
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
