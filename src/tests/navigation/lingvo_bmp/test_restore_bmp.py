#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, param, modal, running, restart


@pytest.mark.navigation_lingvo_bmp
def test_restore_bmp(click, openServiceMenu, db):
    openServiceMenu()
    db.updateValue([
        {'name': param.navigation.backMainPoint, 'value': False}
    ])
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    click(btn.start.play)
    time.sleep(running)
