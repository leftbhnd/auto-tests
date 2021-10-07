#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import pytest

from src.helpers.config import btn, modal, running, restart


@pytest.mark.navigation_self
def test_restore(click, openServiceMenu):
    openServiceMenu()
    os.rename(
        '/home/promobot/.promobot/resources/map.json',
        '/home/promobot/.promobot/resources/map.json_self'
    )
    os.rename(
        '/home/promobot/.promobot/resources/map.json_back',
        '/home/promobot/.promobot/resources/map.json'
    )
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    click(btn.start.play)
    time.sleep(running)
