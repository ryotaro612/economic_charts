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

def fetch(subject_code, line):        
    return list(filter(lambda c: c[2] == subject, line))

if __name__ == '__main__':
    b=[] 
    ngdp_d=[]
    with open('weoreptc.tsv') as f:
        a= [l.split('\t')[:-1] for l in f.readlines()]
        b=list(filter(lambda x: x[9] != '', a))
        ngdp_d = list(filter(lambda x: x[2] == 'NGDP_D', b))
#        for r in f.readlines(:
#            print(len(r.split('\t')[:-1]))

