#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Country:
    def __init__(self, country, weo_subjects):
        self.country = country
        self.weo_subjects = weo_subjects

    def create_gdp_constant_price(self, year):
        # deflator
        ngdp_d = [a for a in list(filter(lambda e: e.code == 'NGDP_D', self.weo_subjects))[0].y_val if a.year == year][0]

        ngdpd_sub = list(filter(lambda e: e.code == 'NGDPD', self.weo_subjects))[0]
        scale = ngdpd_sub.scale
        unit = ngdpd_sub.unit
        ngdpd = [e.val for  e in ngdpd_sub.y_val if  e.year == year ][0]

        print(self.country)
        print(scale)
        print(unit)
        print(ngdp_d.val)
        return ngdpd

    def gdp_constant_usscale_calculable(year):
        return false

    def val_defined(self, subject_code, year):
        subject = get_subject(subject_code) 
        val = [val.val for val in subject.vals if val.year == year][0]
        return val != '' and val != 'n/a'
    """
    def ngdpd_defined(self, year):
        ngdpd = get_subject('NGDPD')
        val = [val.val  for val in ngdpd.vals if val.year == year ][0]
        return val != '' and val != 'n/a'
    """
    def get_subject(self, subject_code):
        "WeoSubject"
        return list(filter(lambda subject: subject.code == subject_code, self.weo_subjects))[0]

class WeoSubject: 
    def __init__(self, code, vals, unit, scale):
        self.code = code
        self.vals = vals
        self.unit = unit
        self.scale = scale

class Val:
    def __init__(self, year, val):
        self.year =  year
        self.val = val

def fetch(subject_code, line):        
    return list(filter(lambda c: c[2] == subject_code, line))

def create_subject(line):
    code = line[2]
    unit = line[6]
    scale = line[7]
    return WeoSubject(code, [Val(a[1], line[a[0]])  for a in zip(range(9,46), range(1980, 2017))], unit, scale)   

def create_ngdp_d(line):
    code = 'NGDP_D'
    unit = line[6]
    scale = line[7]
    return WeoSubject(code, [Val(a[1], line[a[0]])  for a in zip(range(9,46), range(1980, 2017))], unit, scale) 

if __name__ == '__main__':

    with open('weoreptc.tsv') as f:
        lines = [l.split('\t')[:-1] for l in f.readlines()]
        filled_lines = list(filter(lambda x: x[9] != '', lines))
        subjects = [(s[3], create_subject(s)) for s in filled_lines]
#        ngdp_d = list(filter(lambda x: x[2] == 'NGDP_D', b))
        countries= [a for a in set([a[0] for a in subjects])]


        #lambda x: filter(lambda a: a == x, subjects)
        country_subs = list(map(lambda country: Country(country, list(map(lambda x: x[1], filter(lambda s: s[0] == country, subjects)))), countries))
