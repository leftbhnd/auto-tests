#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import internet, interaction
from src.helpers.messages import InteractionMsg, AsrTtsMsg


@pytest.mark.interaction_internet_answer
def test_start_interaction(node):
    interaction_msg = InteractionMsg(True, 0)
    node.interactionPub(interaction_msg)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_internet_answer
def test_internet_type_4(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('где снимался том круз')
    node.asrPub(asr_msg)
    time.sleep(internet)
    assert node.getAnswer() == ''


@pytest.mark.interaction_internet_answer
def test_internet_type_401(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('лучшие комедии')
    node.asrPub(asr_msg)
    time.sleep(internet)
    assert node.getAnswer() == ''


@pytest.mark.interaction_internet_answer
def test_internet_type_6(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('сколько тонн в барреле')
    node.asrPub(asr_msg)
    time.sleep(internet)
    assert node.getAnswer() == ''


@pytest.mark.interaction_internet_answer
def test_internet_type_8(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('сколько ехать до можги')
    node.asrPub(asr_msg)
    time.sleep(internet)
    assert node.getAnswer() == ''


@pytest.mark.interaction_internet_answer
def test_internet_type_9(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('расстояние до альфа-центавра')
    node.asrPub(asr_msg)
    time.sleep(internet)
    assert node.getAnswer() == ''


@pytest.mark.interaction_internet_answer
def test_internet_type_10(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('что такое атмосфера')
    node.asrPub(asr_msg)
    time.sleep(internet)
    assert node.getAnswer() == ''


@pytest.mark.interaction_internet_answer
def test_internet_type_13(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('2гис')
    node.asrPub(asr_msg)
    time.sleep(internet)
    assert node.getAnswer() == ''


@pytest.mark.interaction_internet_answer
def test_internet_type_14(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('300 долларов')
    node.asrPub(asr_msg)
    time.sleep(internet)
    assert node.getAnswer() == ''


@pytest.mark.interaction_internet_answer
def test_internet_type_15(node):
    node.cancelSpeechPub()
    asr_msg = AsrTtsMsg('время в москве')
    node.asrPub(asr_msg)
    time.sleep(internet)
    assert node.getAnswer() == ''


@pytest.mark.interaction_internet_answer
def test_restore(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
