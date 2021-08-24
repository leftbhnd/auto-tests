#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmltodict
import json
import glob, os
os.chdir("./")

for file in glob.glob("*.png"):
    print(file)


data = open('./test.xml', 'r', encoding='utf-8').read()

xpars = xmltodict.parse(data)
test = json.dumps(xpars)