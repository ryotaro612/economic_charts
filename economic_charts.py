#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Country:
    def __init__(self, country, weo_subjects):
        ":"
class WeoSubject: 
    def __init__(self, code, y_val, unit, scale):
        ""

class Val:
    def __init__(self, year, val):
        ""

if __name__ == '__main__':
    with open('weoreptc.tsv') as f:
        for r in f.readlines():
            print(r.split('\t')[:-1])

