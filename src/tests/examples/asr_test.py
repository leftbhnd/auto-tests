#!/usr/bin/env python
# -*- coding: utf-8 -*-

from main import AutoTest, AsrMsg, ClickMsg
import pytest
import csv

test_data = []

with open('test.csv', 'r') as f:
    f_data = csv.reader(f)
    for element in f_data:
        decode_element = [x.decode('utf-8') for x in element]
        test_data.append(tuple(decode_element))


def test_interaction(mouseClick):
    click_msg = ClickMsg(100, 100, 1)
    mouseClick(click_msg)


@pytest.mark.parametrize("question, uuid, answer", test_data)
def test_asr(question, uuid, answer, node):
    asr_msg = AsrMsg(question, uuid)
    node.cancelSpeech()
    node.asrPub(asr_msg)
    node.answersListner()
    assert node.getAnswer() == answer
