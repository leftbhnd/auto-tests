#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import pytest

from src.helpers.config import btn, modal, running, restart


@pytest.mark.navigation_interaction
def test_setup(click, openServiceMenu, db):
    openServiceMenu()
    os.rename(
        '/home/promobot/.promobot/resources/map.json',
        '/home/promobot/.promobot/resources/map.json_back'
    )
    os.rename(
        '/home/promobot/.promobot/resources/map.json_self',
        '/home/promobot/.promobot/resources/map.json'
    )
    db.updateValue([
        {'name': '/interaction/startByFaceInDrive', 'value': 1},
        {'name': '/interaction/updateByFaceInDrive', 'value': 1},
        {'name': '/interaction/updateBySpeechInDrive', 'value': 1}
    ])
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    click(btn.start.play)
    time.sleep(running)
