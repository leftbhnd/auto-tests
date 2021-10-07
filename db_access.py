#!/usr/bin/env python
# -*- coding: utf-8 -*-

db_name = 'promobot'
login = 'promobot'
password = 'PR)(m0bot1'
update = """update robotsettings
    set value = %s
    where parameter=%s"""
select = """select * from robotsettings
    where parameter=%s"""
