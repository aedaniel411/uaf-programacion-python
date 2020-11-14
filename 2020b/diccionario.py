#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:36:15 2020

@author: daniel
"""
def uromano(n):
    return {
        1:'I',
        2:'II',
        3:'III',
        4:'IV',
        5:'V',
        6:'VI',
        7:'VII',
        8:'VIII',
        9:'IX'}.get(n,'no hay valor')

def udromano(n):
    return {
        1:'X',
        2:'XX',
        3:'XXX',
        4:'XL',
        5:'L',
        6:'LX',
        7:'LXX',
        8:'LXXX',
        9:'XC',
        10:'C'}.get(n,'no hay valor')

n = int (input ('numero a convertir: '))

u = n % 10
d = n // 10

print(udromano(d) ,uromano(u))
