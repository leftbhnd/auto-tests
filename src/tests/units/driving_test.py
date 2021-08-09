#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import pytest
import time


def test_enable_joy_mode(node):
    node.joyModePub()
    node.driveModeListener()
    assert node.getDriveMode() is 0
    time.sleep(3)


def test_enable_auto_mode(node):
    node.autoModePub()
    node.driveModeListener()
    assert node.getDriveMode() is 1
    time.sleep(3)


def test_drive_to_point(node):
    node.toPointPub(3)
    node.pointListener()
    assert node.getCurrentPoint() is 3
    time.sleep(3)


def test_wheels_data(node):
    node.wheelsListener()
    assert node.getWheelsData() is [200, 200]
    time.sleep(3)


def test_enable_joy_mode(node):
    node.joyModePub()
    node.driveModeListener()
    assert node.getDriveMode() is 0
    time.sleep(3)


def test_disable_pause(node):
    node.disableDrivePausePub()
    node.drivePauseListener()
    assert node.getDrivePause() is False
    time.sleep(3)


def test_enable_pause(node):
    node.enableDrivePausePub()
    node.drivePauseListener()
    assert node.getDrivePause() is True


def test_drive_status(node):
    assert node.getDriveStatus() is 2
    time.sleep(3)


def test_charge_state(node):
    assert node.getChargeState() is False
    time.sleep(3)


def test_charge_app(node):
    node.chargeAppPub()
    time.sleep(10)
    node.driveStationListener()
    assert node.getDriveStationStatus() is True


def test_enable_joy_mode(node):
    node.joyModePub()
    node.driveModeListener()
    assert node.getDriveMode() is 0
    time.sleep(3)
