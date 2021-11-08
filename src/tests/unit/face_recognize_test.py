#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.unit
def test_face_recognize(node):
    node.facePub(3, 0, 0, 3, 1.0)
    node.clearFacePub()
    assert node.getInteraction() == [True, 1]


@pytest.mark.unit
def test_get_acquainted(node):
    node.facePub(2, 1, 1632114331, 2, 0.9)
    assert node.getFaceIsAcquainted() == True


@pytest.mark.unit
def test_get_not_acquainted(node):
    node.clearFacePub()
    node.facePub(3, 0, 0, 3, 1.0)
    assert node.getFaceIsAcquainted() == False


@pytest.mark.unit
def test_reset(node):
    node.clearFacePub()
