#!/usr/bin/env python
# -*- coding: utf-8 -*-
filename = input('ファイル名を入力してください：')
num = 0
with open(filename, 'r', encoding='UTF-8') as r:
    for i in r:
        num += 1
        print(f'{num} {i}')