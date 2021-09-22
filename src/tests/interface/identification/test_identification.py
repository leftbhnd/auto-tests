#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import modals, btn, modal
'''
43.64 seconds
'''


@pytest.mark.interface_identification
def test_open_identification(clickOn, typeText, screenDiffChecker):
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.ident)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/identification.png'
    ) is None


@pytest.mark.interface_identification
def test_hide_input(clickOn, typeText, screenDiffChecker):
    clickOn(modal.ident_pwd_input)
    clickOn(btn.choose_numbers)
    typeText('111111')
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_hide_pass.png'
    ) is None


@pytest.mark.interface_identification
def test_visiable_input(clickOn, typeText, screenDiffChecker):
    clickOn(modal.ident_kb_pwd_eye)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_visiable_pass.png'
    ) is None


@pytest.mark.interface_identification
def test_confirm_hide_input_same(clickOn, typeText, screenDiffChecker):
    clickOn(modal.ident_kb_confirm_input)
    clickOn(btn.choose_numbers)
    typeText('111111')
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_visiable_hide_pass_same.png'
    ) is None


@pytest.mark.interface_identification
def test_confirm_hide_input_not_same(clickOn, typeText, screenDiffChecker):
    clickOn(modal.ident_kb_confirm_input)
    clickOn(btn.choose_numbers)
    typeText('1')
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_visiable_hide_pass_not_same.png'
    ) is None


@pytest.mark.interface_identification
def test_save_new_pass(clickOn, screenDiffChecker):
    clickOn(modal.ident_kb_confirm_input)
    clickOn(btn.delete)
    clickOn(modal.ident_kb_save)
    assert screenDiffChecker(
        'interfaces/ident_pass_save.png'
    ) is None


@pytest.mark.interface_identification
def test_wrong_pass(clickOn, typeText, screenDiffChecker):
    time.sleep(modals)
    clickOn(btn.back)
    time.sleep(modals)
    clickOn(btn.control)
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.pwd_ok)
    clickOn(btn.reset_input)
    clickOn(btn.reset_input)
    assert screenDiffChecker(
        'interfaces/ident_wrong_pass.png'
    ) is None


@pytest.mark.interface_identification
def test_correct_new_pass(clickOn, typeText, screenDiffChecker):
    clickOn(modal.pwd_input)
    clickOn(btn.choose_numbers)
    typeText('111111')
    clickOn(modal.pwd_ok)
    assert screenDiffChecker(
        'interfaces/control.png'
    ) is None


@pytest.mark.interface_identification
def test_restore(clickOn, typeText):
    clickOn(btn.ident)
    clickOn(modal.ident_pwd_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.ident_kb_confirm_input)
    clickOn(btn.choose_numbers)
    typeText('123456')
    clickOn(modal.ident_kb_save)
    time.sleep(modals)
    clickOn(btn.back)
    time.sleep(modals)
