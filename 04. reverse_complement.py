# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:53:35 2018

@author: Ainesh.Sewak
"""

# Reverse complement



x = 'CTCTTGATC'

def reverse_complement(pattern):
    y = ''
    for i in pattern:
        if i == 'A':
            y = y + 'T'
        elif i == 'T':
            y = y + 'A'
        elif i == 'G':
            y = y + 'C'
        elif i == 'C':
            y = y + 'G'
    
    y = y[::-1]
    return(y)

reverse_complement('CCAGATC')