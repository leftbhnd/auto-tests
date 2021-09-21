#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.conftest import clickOn
import pytest
import time

from src.helpers.messages import SwipeMsg


def test_test(dNd):
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
