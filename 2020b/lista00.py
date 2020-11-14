#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 350 17:10:37 2020

@author: daniel
"""

mat02 = [[1,2,3], [4,5,6], [7,8,9]]


n = int ( input ("dimension del cuadro? "))
mat01 = [ [0] * n for i in range(n) ]

ren = 0
col = n // 2

for x in range (1,n*n + 1):
    mat01[ren][col] = x
    
    if x % n == 0:
        ren = ren + 1
    else:
        ren = ren - 1
        col = col + 1

    if ren == n:
        ren = 0
    
    if ren < 0:
        ren = n - 1
    
    if col == n:
        col = 0
    
for ren in mat01 :
    for col in ren :
        print ('{:3d}'.format(col), end= '' )
    print()
        
