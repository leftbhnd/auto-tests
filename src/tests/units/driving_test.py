#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import pytest
import time


def test_enable_joy_mode(node):
    node.joyModePub()
    assert node.getDriveMode() == 0


def test_enable_auto_mode(node):
    node.autoModePub()
    assert node.getDriveMode() == 1


def test_drive_to_point(node):
    node.toPointPub(3)
    assert node.getCurrentPoint() == 3


def test_wheels_data(node):
    assert node.getWheelsData() != [0, 0]


def test_enable_joy_mode(node):
    node.joyModePub()
    assert node.getDriveMode() == 0


def test_disable_pause(node):
    node.disableDrivePausePub()
    assert node.getDrivePause() == False


def test_enable_pause(node):
    node.enableDrivePausePub()
    assert node.getDrivePause() == True


def test_drive_status(node):
    assert node.getDriveStatus() in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_charge_state(node):
    assert node.getChargeState() == False


def test_charge_app(node):
    node.chargeAppPub()
    time.sleep(10)
    assert node.getDriveStationStatus() == True


def test_enable_joy_mode(node):
    node.joyModePub()
    assert node.getDriveMode() == 0


def test_use_radius(node):
    assert node.getUseRadius() in [True, False]
