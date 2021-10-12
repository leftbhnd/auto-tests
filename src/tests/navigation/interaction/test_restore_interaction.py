#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import pytest

from src.helpers.config import btn, param, modal, running, restart


@pytest.mark.navigation_interaction
def test_restore(click, openServiceMenu, db):
    openServiceMenu()
    os.rename(
        '/home/promobot/.promobot/resources/map.json',
        '/home/promobot/.promobot/resources/map.json_self'
    )
    os.rename(
        '/home/promobot/.promobot/resources/map.json_back',
        '/home/promobot/.promobot/resources/map.json'
    )
    db.updateValue([
        {'name': param.interaction.startByFaceInDrive, 'value': 0},
        {'name': param.interaction.updateByFaceInDrive, 'value': 0},
        {'name': param.interaction.updateBySpeechInDrive, 'value': 0},
        {'name': param.navigation.ignoreInteractions, 'value': False}
    ])
    click(btn.control.restart)
    click(modal.restart.yes)
    time.sleep(restart)
    click(btn.start.play)
    time.sleep(running)
