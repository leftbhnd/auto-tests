#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import pytest

from src.helpers.messages import FaceMsg


@pytest.mark.skip(reason="unit")
def test_face_recognize(node):
    face_msg = FaceMsg(2, False, 21, 211, 0.9)
    node.facePub(face_msg)
    assert node.getInteraction() == [True, 1]
