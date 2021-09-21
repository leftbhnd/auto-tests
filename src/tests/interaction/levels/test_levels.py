#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals, interaction, running, restart
from src.helpers.messages import SwipeMsg, InteractionMsg, AsrTtsMsg
'''
750 seconds
'''


@pytest.mark.interaction_levels
def test_robot_base(node):
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    asr_msg = AsrTtsMsg('порядок')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'Робот высокий приоритет'


@pytest.mark.interaction_levels
def test_owner_base(clickOn, typeText, openPwdModal, dNd, node):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lingvo)
    clickOn(btn.lingvo_sources)
    clickOn(btn.lingvo_first_level)
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    asr_msg = AsrTtsMsg('порядок')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'Владелец высокий приоритет'


@pytest.mark.interaction_levels
def test_robot_base_low(clickOn, typeText, openPwdModal, dNd, node):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lingvo)
    clickOn(btn.lingvo_sources)
    clickOn(btn.lingvo_first_level)
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    asr_msg = AsrTtsMsg('порядок')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'Робот низкий приоритет'


@pytest.mark.interaction_levels
def test_owner_base_low(clickOn, typeText, openPwdModal, dNd, node):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lingvo)
    clickOn(btn.lingvo_sources)
    clickOn(btn.lingvo_first_level)
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    asr_msg = AsrTtsMsg('порядок')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'Владелец низкий приоритет'


@pytest.mark.interaction_levels
def test_common_base(clickOn, typeText, openPwdModal, dNd, node):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lingvo)
    clickOn(btn.lingvo_sources)
    clickOn(btn.lingvo_first_level)
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    asr_msg = AsrTtsMsg('порядок')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'common base'


@pytest.mark.interaction_levels
def test_internet_base(clickOn, typeText, openPwdModal, dNd, node):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lingvo)
    clickOn(btn.lingvo_sources)
    clickOn(btn.lingvo_first_level)
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    asr_msg = AsrTtsMsg('порядок')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'internet'


@pytest.mark.interaction_levels
def test_common_base_low(clickOn, typeText, openPwdModal, dNd, node):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lingvo)
    clickOn(btn.lingvo_sources)
    clickOn(btn.lingvo_first_level)
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    asr_msg = AsrTtsMsg('порядок')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'common base low'


@pytest.mark.interaction_levels
def test_unrecognized(clickOn, typeText, openPwdModal, dNd, node):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lingvo)
    clickOn(btn.lingvo_sources)
    clickOn(btn.lingvo_first_level)
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    asr_msg = AsrTtsMsg('порядок')
    node.asrPub(asr_msg)
    assert node.getAnswer() == 'нераспознанная фраза'


@pytest.mark.interaction_levels
def test_restore(clickOn, typeText, openPwdModal, dNd, node):
    openPwdModal()
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.settings)
    clickOn(btn.lingvo)
    clickOn(btn.lingvo_sources)
    clickOn(btn.lingvo_first_level)
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
    clickOn(btn.back)
    clickOn(modal.save_yes)
    time.sleep(modals)
    clickOn(btn.back)
    clickOn(btn.restart)
    clickOn(modal.restart_yes)
    time.sleep(restart)
    clickOn(btn.play)
    clickOn(modal.radius_yes)
    time.sleep(running)
    time.sleep(interaction)
    assert node.getLevelsOrder() == ['0', '1', '2', '3', '4', '5', '6', '7']
