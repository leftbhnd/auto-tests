#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.unit
def test_get_default(db):
    assert db.get(
        'robot_settings/driving/radius'
    ) == ['robot_settings/driving/radius', '5']


@pytest.mark.unit
def test_set(db):
    assert db.update(3, 'robot_settings/driving/radius') == 1


@pytest.mark.unit
def test_get_new(db):
    assert db.get(
        'robot_settings/driving/radius'
    ) == ['robot_settings/driving/radius', '3']


@pytest.mark.unit
def test_restore_default(db):
    assert db.update(5, 'robot_settings/driving/radius') == 1


@pytest.mark.unit
def test_check_default(db):
    assert db.get(
        'robot_settings/driving/radius'
    ) == ['robot_settings/driving/radius', '5']
