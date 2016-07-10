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
        self.year =  year
        self.val = val

def fetch(subject_code, line):        
    return list(filter(lambda c: c[2] == subject_code, line))
   
def create_ngdp_d(line):
    code = 'NGDP_D'
    unit = line[6]
    scale = line[7]
    return  [Val(a[1], line[a[0]])  for a in zip(range(9,46), range(1980, 2017))]

if __name__ == '__main__':
    b=[] 
    ngdp_d=[]
    ngdpd=[]
    with open('weoreptc.tsv') as f:
        a= [l.split('\t')[:-1] for l in f.readlines()]
        b=list(filter(lambda x: x[9] != '', a))
        ngdp_d = fetch('NGDP_D', b)
        ngdpd = fetch('NGDPD', b)
#        ngdp_d = list(filter(lambda x: x[2] == 'NGDP_D', b))

