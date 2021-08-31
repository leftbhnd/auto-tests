#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time


@pytest.mark.skip(reason="unit")
def test_enable_joy_mode(node):
    node.initNode()
    node.joyModePub()
    assert node.getDriveMode() == 0


@pytest.mark.skip(reason="unit")
def test_enable_auto_mode(node):
    node.autoModePub()
    assert node.getDriveMode() == 1


@pytest.mark.skip(reason="unit")
def test_drive_to_point(node):
    node.toPointPub(3)
    assert node.getCurrentPoint() == 3


@pytest.mark.skip(reason="unit")
def test_wheels_data(node):
    assert node.getWheelsData() != [0, 0]


@pytest.mark.skip(reason="unit")
def test_enable_joy_mode(node):
    node.joyModePub()
    assert node.getDriveMode() == 0


@pytest.mark.skip(reason="unit")
def test_disable_pause(node):
    node.disableDrivePausePub()
    assert node.getDrivePause() == False


@pytest.mark.skip(reason="unit")
def test_enable_pause(node):
    node.enableDrivePausePub()
    assert node.getDrivePause() == True


@pytest.mark.skip(reason="unit")
def test_drive_status(node):
    assert node.getDriveStatus() in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.skip(reason="unit")
def test_charge_state(node):
    assert node.getChargeState() == False


@pytest.mark.skip(reason="unit")
def test_charge_app(node):
    node.chargeAppPub()
    time.sleep(10)
    assert node.getDriveStationStatus() == True


@pytest.mark.skip(reason="unit")
def test_enable_joy_mode(node):
    node.joyModePub()
    assert node.getDriveMode() == 0


@pytest.mark.skip(reason="unit")
def test_use_radius(node):
    assert node.getUseRadius() in [True, False]


@pytest.mark.skip(reason="unit")
def test_finish(node):
    node.killNode()
