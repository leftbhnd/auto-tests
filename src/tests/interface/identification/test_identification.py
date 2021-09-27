#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, modals
'''
35.53 seconds
'''


@pytest.mark.interface_identification
def test_open_identification(click, typeText, screenDiffChecker):
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.control.ident)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/identification.png'
    ) is None


@pytest.mark.interface_identification
def test_hide_input(click, typeText, screenDiffChecker):
    click(modal.ident.input)
    click(btn.kb.numbers)
    typeText('111111')
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/ident_hide_pass.png'
    ) is None


@pytest.mark.interface_identification
def test_visiable_input(click, screenDiffChecker):
    click(modal.ident.kb_eye)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/ident_visiable_pass.png'
    ) is None


@pytest.mark.interface_identification
def test_confirm_hide_input_same(click, typeText, screenDiffChecker):
    click(modal.ident.kb_confirm_input)
    click(btn.kb.numbers)
    typeText('111111')
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/ident_visiable_hide_pass_same.png'
    ) is None


@pytest.mark.interface_identification
def test_confirm_hide_input_not_same(click, typeText, screenDiffChecker):
    click(modal.ident.kb_confirm_input)
    click(btn.kb.numbers)
    typeText('1')
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/ident_visiable_hide_pass_not_same.png'
    ) is None


@pytest.mark.interface_identification
def test_save_new_pass(click, screenDiffChecker):
    click(modal.ident.kb_confirm_input)
    click(btn.kb.delete)
    click(modal.ident.kb_save)
    assert screenDiffChecker(
        'interfaces/ident_pass_save.png'
    ) is None


@pytest.mark.interface_identification
def test_wrong_pass(click, typeText, screenDiffChecker):
    time.sleep(modals)
    click(btn.handler.back)
    time.sleep(modals)
    click(btn.start.control)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.pwd.ok)
    click(btn.handler.reset)
    click(btn.handler.reset)
    assert screenDiffChecker(
        'interfaces/ident_wrong_pass.png'
    ) is None


@pytest.mark.interface_identification
def test_correct_new_pass(click, typeText, screenDiffChecker):
    click(modal.pwd.input)
    click(btn.kb.numbers)
    typeText('111111')
    click(modal.pwd.ok)
    assert screenDiffChecker(
        'interfaces/control.png'
    ) is None


@pytest.mark.interface_identification
def test_restore(click, typeText):
    click(btn.control.ident)
    click(modal.ident.input)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.ident.kb_confirm_input)
    click(btn.kb.numbers)
    typeText('123456')
    click(modal.ident.kb_save)
    time.sleep(modals)
    click(btn.handler.back)
    time.sleep(modals)
