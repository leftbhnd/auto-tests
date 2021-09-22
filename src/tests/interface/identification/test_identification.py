#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
43.64 seconds
'''


@pytest.mark.interface_identification
def test_open_identification(click, type, screenDiffChecker):
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.ident)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/identification.png'
    ) is None


@pytest.mark.interface_identification
def test_hide_input(click, type, screenDiffChecker):
    click(modal.ident_pwd_input)
    click(btn.choose_numbers)
    type('111111')
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_hide_pass.png'
    ) is None


@pytest.mark.interface_identification
def test_visiable_input(click, type, screenDiffChecker):
    click(modal.ident_kb_pwd_eye)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_visiable_pass.png'
    ) is None


@pytest.mark.interface_identification
def test_confirm_hide_input_same(click, type, screenDiffChecker):
    click(modal.ident_kb_confirm_input)
    click(btn.choose_numbers)
    type('111111')
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_visiable_hide_pass_same.png'
    ) is None


@pytest.mark.interface_identification
def test_confirm_hide_input_not_same(click, type, screenDiffChecker):
    click(modal.ident_kb_confirm_input)
    click(btn.choose_numbers)
    type('1')
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_visiable_hide_pass_not_same.png'
    ) is None


@pytest.mark.interface_identification
def test_save_new_pass(click, screenDiffChecker):
    click(modal.ident_kb_confirm_input)
    click(btn.delete)
    click(modal.ident_kb_save)
    assert screenDiffChecker(
        'interfaces/ident_pass_save.png'
    ) is None


@pytest.mark.interface_identification
def test_wrong_pass(click, type, screenDiffChecker):
    time.sleep(modals)
    click(btn.back)
    time.sleep(modals)
    click(btn.control)
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.pwd_ok)
    click(btn.reset_input)
    click(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_wrong_pass.png'
    ) is None


@pytest.mark.interface_identification
def test_correct_new_pass(click, type, screenDiffChecker):
    click(modal.pwd_input)
    click(btn.choose_numbers)
    type('111111')
    click(modal.pwd_ok)
    assert screenDiffChecker(
        'interfaces/control.png'
    ) is None


@pytest.mark.interface_identification
def test_restore(click, type):
    click(btn.ident)
    click(modal.ident_pwd_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.ident_kb_confirm_input)
    click(btn.choose_numbers)
    type('123456')
    click(modal.ident_kb_save)
    time.sleep(modals)
    click(btn.back)
    time.sleep(modals)
