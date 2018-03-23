# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 23:48:08 2018

@author: Ainesh
"""



pattern = 'TACAG'
text = 'GAATCCGCCAAGTACCAAGATGTAAGTGAGGAGCGCTTAGGTCTGTACTGCGCATAAGCCTTAACGCGAAGTATGGATATGCTCCCCGGATACAGGTTTGGGATTTGGCGGTTACCTAAGCTAACGGTGAGACCGATATGACGAGGTTCCTATCTTAATCATATTCACATACTGAACGAGGCGCCCAGTTTCTTCTCACCAATATGTCAGGAAGCTACAGTGCAGCATTATCCACACCATTCCACTTATCCTTGAACGGAAGTCTTATGCGAAGATTATTCTGAGAAGCCCTTGTGCCCTGCATCACGATTTGCAGACTGACAGGGAATCTTAAGGCCACTCAAA'
d = 2




with open('C:/Users/Ainesh/Downloads/dataset_9_6.txt') as f:
    file = f.read().splitlines()
    
pattern = file[0]
text = file[1]
d = int(file[2])


def hamming_distance(p, q):
    out = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            out += 1
    return(out)
    

def approximate_pattern_count(pattern, text, d):
    approximate_pattern_frequency = 0
    pattern_length = len(pattern)
    for i in range(0, len(text) - pattern_length + 1):
        pattern_in_text = text[ i : i + pattern_length]
        hd_pattern = hamming_distance(pattern, pattern_in_text)
        if hd_pattern <= d:
            approximate_pattern_frequency += 1
    
    print(approximate_pattern_frequency)

approximate_pattern_count(pattern, text, d)
    



