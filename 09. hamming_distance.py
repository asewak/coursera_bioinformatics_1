# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:58:31 2018

@author: Ainesh
"""

p = 'GGGCCGTTGGT'
q = 'GGACCGTTGAC'

def hamming_distance(p, q):
    out = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            out += 1
    print(out)
    
with open('C:/Users/Ainesh/Downloads/dataset_9_3.txt') as f:
    file = f.read().splitlines()
    
p = file[0]
q = file[1]