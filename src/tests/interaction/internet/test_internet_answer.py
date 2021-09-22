#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import internet, interaction
'''
73.28 seconds
'''


@pytest.mark.interaction_internet_answer
def test_start_interaction(node):
    node.interactionPub(True, 0)
    assert node.getInteraction() == [True, 0]


@pytest.mark.interaction_internet_answer
def test_internet_type_4(node):
    node.cancelSpeechPub()
    node.asrPub('где снимался том круз')
    time.sleep(internet)
    assert node.getAnswer() == 'Том Круз, Фильмы: Миссия невыполнима (1996 год), Топ Ган: Мэверик (2022 год), Миссия невыполнима: Последствия (2018 год) и другие.'


@pytest.mark.interaction_internet_answer
def test_internet_type_401(node):
    node.cancelSpeechPub()
    node.asrPub('лучшие комедии')
    time.sleep(internet)
    assert node.getAnswer(
    ) == 'Популярные комедии: Ведьмы, Круэлла, Космический джем: Новое поколение и другие.'


@pytest.mark.interaction_internet_answer
def test_internet_type_6(node):
    node.cancelSpeechPub()
    node.asrPub('сколько тонн в барреле')
    time.sleep(internet)
    assert node.getAnswer() == '1 баррель (американский, нефтяной) ≈ 0,14 тонн нефти (в среднем по США, более точно зависит от марки нефти и температуры/плотности) = 136,40 кг нефти.'


@pytest.mark.interaction_internet_answer
def test_internet_type_8(node):
    node.cancelSpeechPub()
    node.asrPub('сколько ехать до можги')
    time.sleep(internet)
    assert node.getAnswer() == 'Маршрут: E22, 5 ч 15 минут, 371,80 километров'


@pytest.mark.interaction_internet_answer
def test_internet_type_9(node):
    node.cancelSpeechPub()
    node.asrPub('расстояние до альфа-центавра')
    time.sleep(internet)
    assert node.getAnswer() == 'Альфа Центавра, Расстояние до Земли, 4,37 световых лет'


@pytest.mark.interaction_internet_answer
def test_internet_type_10(node):
    node.cancelSpeechPub()
    node.asrPub('что такое атмосфера')
    time.sleep(internet)
    assert node.getAnswer() == 'Атмосфера — газовая оболочка небесного тела, удерживаемая около него гравитацией. Поскольку не существует резкой границы между атмосферой и межпланетным пространством, то обычно атмосферой принято считать область вокруг небесного тела, в которой газовая среда вращается вместе с ним как единое целое.'


@pytest.mark.interaction_internet_answer
def test_internet_type_13(node):
    node.cancelSpeechPub()
    node.asrPub('miro')
    time.sleep(internet)
    assert node.getAnswer() == 'Miro — платформа для совместной работы распределенных команд, разработанная в России и вышедшая на международный рынок.'


@pytest.mark.interaction_internet_answer
def test_restore(node):
    node.cancelSpeechPub()
    time.sleep(interaction)
