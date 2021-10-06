#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, running, restart


@pytest.mark.navigation_lingvo_mp
def test_setup_bmp(click, openServiceMenu, db):
    openServiceMenu()
    db.updateValue([
        {'name': '/navigation/backMainPoint/', 'value': True}
    ])
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    click(btn.start.play)
    time.sleep(running)
