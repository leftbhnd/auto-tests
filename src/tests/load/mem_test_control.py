#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time
'''
X seconds
'''


@pytest.mark.load_test
def test_memory(raw_click):
    while True:
        raw_click((3048, 577))
        time.sleep(6)
