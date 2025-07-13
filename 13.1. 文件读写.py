#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#读文件
from datetime import datetime


with open('/Users/ACER/Desktop/testfile.txt','r',encoding='utf-8') as f:
    print(f.read())


#写文件
with open('/Users/ACER/Desktop/testfile.txt','w',encoding='utf-8') as f:
    f.write('niubi')

with open('/Users/ACER/Desktop/testfile.txt','a',encoding='utf-8') as f:
    f.write('\ntainiubile')
    f.write(datetime.now().strftime("%Y-%m-%d"))