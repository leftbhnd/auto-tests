#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time


@pytest.mark.skip(reason="unit")
def test_volume_up(node, joy):
    joy_msg = joy.upVolume()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]


@pytest.mark.skip(reason="unit")
def test_volume_down(node, joy):
    joy_msg = joy.downVolume()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]


@pytest.mark.skip(reason="unit")
def test_mic_up(node, joy):
    joy_msg = joy.upMic()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]


@pytest.mark.skip(reason="unit")
def test_mic_down(node, joy):
    joy_msg = joy.downMic()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]


@pytest.mark.skip(reason="unit")
def test_phrase_mode_enable(node, joy):
    joy_msg = joy.phraseMode()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]


@pytest.mark.skip(reason="unit")
def test_next_phrase(node, joy):
    joy_msg = joy.nextPhrase()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]


@pytest.mark.skip(reason="unit")
def test_previous_phrase(node, joy):
    joy_msg = joy.previousPhrase()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]


@pytest.mark.skip(reason="unit")
def test_phrase_mode_disable(node, joy):
    joy_msg = joy.phraseMode()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]


@pytest.mark.skip(reason="unit")
def test_auto_mode_enable(node, joy):
    joy_msg = joy.autoMode()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]


@pytest.mark.skip(reason="unit")
def test_auto_mode_disable(node, joy):
    joy_msg = joy.autoMode()
    node.joyCommandPub(joy_msg)
    time.sleep(3)
    assert node.getJoyCmd() == [
        (0.0, 0.0, 0.0, 0.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]
