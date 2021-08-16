#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

'''
79.94 seconds
'''


@pytest.mark.identification
def test_open_identification(clickOn, typeText, screenDiffChecker):
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('identification')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker('identification.png') is None


@pytest.mark.identification
def test_hide_input(clickOn, typeText, screenDiffChecker):
    clickOn('ident_modal_pass_input')
    clickOn('choose_numbers')
    typeText(['1', '1', '1', '1', '1', '1'])
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker('ident_hide_pass.png') is None


@pytest.mark.identification
def test_visiable_input(clickOn, typeText, screenDiffChecker):
    clickOn('kb_ident_modal_pass_eye')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker('ident_visiable_pass.png') is None


@pytest.mark.identification
def test_confirm_hide_input_same(clickOn, typeText, screenDiffChecker):
    clickOn('kb_ident_modal_confirm_input')
    clickOn('choose_numbers')
    typeText(['1', '1', '1', '1', '1', '1'])
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker('ident_visiable_hide_pass_same.png') is None


@pytest.mark.identification
def test_confirm_hide_input_not_same(clickOn, typeText, screenDiffChecker):
    clickOn('kb_ident_modal_confirm_input')
    clickOn('choose_numbers')
    typeText(['1'])
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker('ident_visiable_hide_pass_not_same.png') is None


@pytest.mark.identification
def test_save_new_pass(clickOn, typeText, screenDiffChecker):
    clickOn('kb_ident_modal_confirm_input')
    typeText('d')
    clickOn('kb_ident_modal_save')
    assert screenDiffChecker('ident_pass_save.png') is None


@pytest.mark.identification
def test_wrong_pass(clickOn, typeText, screenDiffChecker):
    time.sleep(4)
    clickOn('back')
    time.sleep(4)
    clickOn('control')
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('pass_modal_ok')
    clickOn('reset_input')
    clickOn('reset_input')
    assert screenDiffChecker('ident_wrong_pass.png') is None


@pytest.mark.identification
def test_correct_new_pass(clickOn, typeText, screenDiffChecker):
    clickOn('pass_modal_input')
    clickOn('choose_numbers')
    typeText(['1', '1', '1', '1', '1', '1'])
    clickOn('pass_modal_ok')
    assert screenDiffChecker('control.png') is None


@pytest.mark.identification
def test_restore(clickOn, typeText, screenDiffChecker):
    clickOn('identification')
    clickOn('ident_modal_pass_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('kb_ident_modal_confirm_input')
    clickOn('choose_numbers')
    typeText(['1', '2', '3', '4', '5', '6'])
    clickOn('kb_ident_modal_save')
    time.sleep(4)
    clickOn('restart')
    clickOn('restart_modal_yes')
    time.sleep(40)
    assert screenDiffChecker('start.png') is None
