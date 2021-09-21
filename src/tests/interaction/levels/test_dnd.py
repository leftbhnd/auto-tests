#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.conftest import clickOn
import pytest
import time

from src.helpers.config import btn
from src.helpers.messages import SwipeMsg


def test_test(clickOn, dNd):
    clickOn(btn.lingvo_first_level)
    time.sleep(5)
    swipe_msg = SwipeMsg((446, 233), (446, 655))
    dNd(swipe_msg)
