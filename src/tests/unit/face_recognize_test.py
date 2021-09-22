#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.unit
def test_face_recognize(node):
    node.facePub(3, 0, 0, 3, 1.0)
    node.clearFacePub()
    assert node.getInteraction() == [True, 1]
