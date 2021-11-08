#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, case_timeout, case_test_pause


@pytest.mark.acquaintance
def test_acquaintance(node, click):
    while True:
        if node.getFaceIsAcquainted() == False:
            click(btn.savelovsky.start)
            time.sleep(case_timeout)
            click(btn.savelovsky.kb_a)
            click(btn.savelovsky.name)
            click(btn.savelovsky.kb_a)
            click(btn.savelovsky.phone)
            for i in range(10):
                click(btn.savelovsky.kb_number)
            click(btn.savelovsky.confirm)
            click(btn.savelovsky.save)
            time.sleep(case_timeout)
            click(btn.savelovsky.free_enter)
            click(btn.savelovsky.choose)
            time.sleep(case_timeout)
            click(btn.savelovsky.get_check)
            time.sleep(case_test_pause)
        else:
            time.sleep(case_test_pause)
