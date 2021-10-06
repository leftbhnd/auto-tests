#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2

from db_access import db_name, login, password, update, select


class DbRequest:
    def __init__(self):
        self._connection = psycopg2.connect(
            dbname=db_name, user=login,
            password=password
        )
        self._cursor = self._connection.cursor()
        self._update = update
        self._select = select
        self._updated_rows = 0

    def _closeConnection(self):
        self._cursor.close()
        self._connection.close()

    def _createParamName(self, name):
        return 'robot_settings' + name

    def updateValue(self, params):
        for param in params:
            self._cursor.execute(
                self._update, (
                    param['value'],
                    self._createParamName(param['name'])
                )
            )
            self._updated_rows += self._cursor.rowcount
        self._connection.commit()
        self._closeConnection()
        return self._updated_rows

    def getValue(self, param):
        self._cursor.execute(
            self._select, (
                self._createParamName(param),
            )
        )
        for row in self._cursor:
            return row[3]
        self._closeConnection()
