# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 23:00:26 2018

@author: Ainesh
"""

# put your python code here

import sys

file = sys.stdin.read().splitlines()
genome = file[0]

def skew(genome):
    out = [0]
    for i in range(0, len(genome)):
        if genome[i] == 'G':
            out.append(out[i]+1)
        elif genome[i] == 'C':
            out.append(out[i]-1)
        else:
            out.append(out[i])
    
    #print(' '.join(map(str,out)))
    return(out)

skew_g = skew(genome)
skew_min = min(skew_g)
min_skew_idx = [i for i, x in enumerate(skew_g) if x == skew_min]
print(' '.join(map(str,min_skew_idx)))



