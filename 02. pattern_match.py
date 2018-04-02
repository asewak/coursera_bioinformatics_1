# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:38:52 2018

@author: Ainesh.Sewak
"""

#pattern match

import re

pattern = 'TGCGAGATG'
genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'


def pattern_match(pattern, genome):
    pattern_regex = '(?=' + pattern + ')'
    iter = re.finditer(pattern_regex, genome)
    indices = [m.start(0) for m in iter]
    out = ' '.join(map(str, indices))
    print(out)

pattern_match(pattern, genome)


#iter = re.finditer(pattern_regex, genome)

#y = ''
#for m in iter:
    
 #   y = y + ' ' + str(m.start())
 
 
with open('C:/Users/ainesh.sewak/Downloads/Vibrio_cholerae.txt') as f:
    file = f.read().splitlines()

# Where CTTGATCAT appears as a substring in the Vibrio cholerae genome
pattern_match('CTTGATCAT', file[0])
pattern_match('ATGATCAAG', file[0])