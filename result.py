#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import re

suite = ''
tests = []
reg = r'(?<=src/tests/)[\w_/.: ]+(?=[ \d%])'


data = open('./test.txt', 'r', encoding='utf-8').read()
parsed = re.findall(reg, data)

for line in parsed:
    line = re.sub(r'::', ' ', line).split()
    tests.append({'test_name': line[1], 'test_result': line[2]})
    suite = line[0]


result_obj = {'suite': suite, 'test-cases': tests}

payload = json.dumps(result_obj)
print(payload)

requests.post('http://127.0.0.1/post', data=payload)
