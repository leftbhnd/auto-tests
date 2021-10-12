#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, param, modal, restart


@pytest.mark.navigation_restore
def test_restore(click, openServiceMenu, db):
    db.updateValue([
        {'name': param.driving.useMap, 'value': False},
        {'name': param.driving.useRadius, 'value': True}
    ])
    openServiceMenu()
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
