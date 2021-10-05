#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

from db_access import login, password


class DbRequest:
    def __init__(self):
        self._connection = psycopg2.connect(
            dbname='promobot', user=login,
            password=password
        )
        self._cursor = self._connection.cursor()
        self._update = """update robotsettings
            set value = %s
            where parameter=%s"""
        self._updated_rows = 0

    def update(self, value, param):
        self._cursor.execute(
            self._update, (value, param)
        )
        self._updated_rows = self._cursor.rowcount
        self._connection.commit()
        self._cursor.close()
        self._connection.close()
        return self._updated_rows

    def get(self, param):
        self._cursor.execute(
            'select * from robotsettings where parameter=%s', (
                param,
            )
        )
        for row in self._cursor:
            return [row[2], row[3]]
        self._cursor.close()
        self._connection.close()
