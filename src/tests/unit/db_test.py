#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from src.helpers.config import param


@pytest.mark.unit
def test_get_default(db):
    assert db.getValue(param.driving.radius) == '5'


@pytest.mark.unit
def test_update_value(db):
    assert db.updateValue([{'name': param.driving.radius, 'value': 3}]) == 1


@pytest.mark.unit
def test_get_new_value(db):
    assert db.getValue(param.driving.radius) == '3'


@pytest.mark.unit
def test_restore_default_value(db):
    assert db.updateValue([{'name': param.driving.radius, 'value': 5}]) == 1


@pytest.mark.unit
def test_check_default_value(db):
    assert db.getValue(param.driving.radius) == '5'


@pytest.mark.unit
def test_map_on(db):
    assert db.updateValue([
        {'name': param.driving.useMap, 'value': True},
        {'name': param.driving.useRadius, 'value': False}
    ]) == 2


@pytest.mark.unit
def test_map_get_value_use_map(db):
    assert db.getValue(param.driving.useMap) == 'true'


@pytest.mark.unit
def test_map_get_value_use_radius(db):
    assert db.getValue(param.driving.useRadius) == 'false'


@pytest.mark.unit
def test_radius_on(db):
    assert db.updateValue([
        {'name': param.driving.useMap, 'value': False},
        {'name': param.driving.useRadius, 'value': True}
    ]) == 2


@pytest.mark.unit
def test_radius_get_value_use_map(db):
    assert db.getValue(param.driving.useMap) == 'false'


@pytest.mark.unit
def test_radius_get_value_use_radius(db):
    assert db.getValue(param.driving.useRadius) == 'true'


@pytest.mark.unit
def test_bmp_on(db):
    assert db.updateValue([
        {'name': param.navigation.backMainPoint, 'value': True}
    ]) == 1


@pytest.mark.unit
def test_bmp_on_get(db):
    assert db.getValue(param.navigation.backMainPoint) == 'true'


@pytest.mark.unit
def test_bmp_off(db):
    assert db.updateValue([
        {'name': param.navigation.backMainPoint, 'value': False}
    ]) == 1


@pytest.mark.unit
def test_bmp_off_get(db):
    assert db.getValue(param.navigation.backMainPoint) == 'false'


@pytest.mark.unit
def test_ignoreInteraction_on(db):
    assert db.updateValue([
        {'name': param.navigation.ignoreInteractions, 'value': True}
    ]) == 1


@pytest.mark.unit
def test_ignoreInteraction_on_get(db):
    assert db.getValue(param.navigation.ignoreInteractions) == 'true'


@pytest.mark.unit
def test_ignoreInteraction_off(db):
    assert db.updateValue([
        {'name': param.navigation.ignoreInteractions, 'value': False}
    ]) == 1


@pytest.mark.unit
def test_ignoreInteraction_off_get(db):
    assert db.getValue(param.navigation.ignoreInteractions) == 'false'
