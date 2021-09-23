#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, interaction, running, restart
'''
750 seconds
'''


@pytest.mark.interaction_levels
def test_robot_base(node):
    node.interactionPub(True, 0)
    node.asrPub('порядок')
    assert node.getAnswer() == 'Робот высокий приоритет'


@pytest.mark.interaction_levels
def test_owner_base(click, dNd, openServiceMenu, node):
    openServiceMenu()
    click(btn.settings)
    click(btn.lingvo)
    click(btn.lingvo_sources)
    click(btn.lingvo_first_level)
    dNd((446, 233), (446, 655))
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    node.interactionPub(True, 0)
    node.asrPub('порядок')
    assert node.getAnswer() == 'Владелец высокий приоритет'


@pytest.mark.interaction_levels
def test_robot_base_low(click, dNd, openServiceMenu, node):
    openServiceMenu()
    click(btn.settings)
    click(btn.lingvo)
    click(btn.lingvo_sources)
    click(btn.lingvo_first_level)
    dNd((446, 233), (446, 655))
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    node.interactionPub(True, 0)
    node.asrPub('порядок')
    assert node.getAnswer() == 'Робот низкий приоритет'


@pytest.mark.interaction_levels
def test_owner_base_low(click, dNd, openServiceMenu, node):
    openServiceMenu()
    click(btn.settings)
    click(btn.lingvo)
    click(btn.lingvo_sources)
    click(btn.lingvo_first_level)
    dNd((446, 233), (446, 655))
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    node.interactionPub(True, 0)
    node.asrPub('порядок')
    assert node.getAnswer() == 'Владелец низкий приоритет'


@pytest.mark.interaction_levels
def test_common_base(click, dNd, openServiceMenu, node):
    openServiceMenu()
    click(btn.settings)
    click(btn.lingvo)
    click(btn.lingvo_sources)
    click(btn.lingvo_first_level)
    dNd((446, 233), (446, 655))
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    node.interactionPub(True, 0)
    node.asrPub('порядок')
    assert node.getAnswer() == 'common base'


@pytest.mark.interaction_levels
def test_internet_base(click, dNd, openServiceMenu, node):
    openServiceMenu()
    click(btn.settings)
    click(btn.lingvo)
    click(btn.lingvo_sources)
    click(btn.lingvo_first_level)
    dNd((446, 233), (446, 655))
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    node.interactionPub(True, 0)
    node.asrPub('порядок')
    assert node.getAnswer() == 'internet'


@pytest.mark.interaction_levels
def test_common_base_low(click, dNd, openServiceMenu, node):
    openServiceMenu()
    click(btn.settings)
    click(btn.lingvo)
    click(btn.lingvo_sources)
    click(btn.lingvo_first_level)
    dNd((446, 233), (446, 655))
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    node.interactionPub(True, 0)
    node.asrPub('порядок')
    assert node.getAnswer() == 'common base low'


@pytest.mark.interaction_levels
def test_unrecognized(click, dNd, openServiceMenu, node):
    openServiceMenu()
    click(btn.settings)
    click(btn.lingvo)
    click(btn.lingvo_sources)
    click(btn.lingvo_first_level)
    dNd((446, 233), (446, 655))
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    node.interactionPub(True, 0)
    node.asrPub('порядок')
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_restore(click, dNd, openServiceMenu, node):
    openServiceMenu()
    click(btn.settings)
    click(btn.lingvo)
    click(btn.lingvo_sources)
    click(btn.lingvo_first_level)
    dNd((446, 233), (446, 655))
    click(btn.back)
    click(modal.save_yes)
    time.sleep(modals)
    click(btn.back)
    click(btn.restart)
    click(modal.restart_yes)
    time.sleep(restart)
    click(btn.play)
    click(modal.radius_yes)
    time.sleep(running)
    time.sleep(interaction)
    assert node.getLevelsOrder() == ['0', '1', '2', '3', '4', '5', '6', '7']
