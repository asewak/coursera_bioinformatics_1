# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 20:54:41 2018

@author: Ainesh.Sewak
"""


def hamming_distance(p, q):
    out = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            out += 1
    return(out)

def neigbours(pattern, d):
    unique_letters = 'ACGT'
    if d == 0:
        return(pattern)
    if len(pattern) == 1:
        return({'A', 'C', 'G', 'T'})
    neigbourhood = set()
    suffix_pattern = pattern[1:]
    suffix_neigbours = neigbours(suffix_pattern, d)
    for s in suffix_neigbours:
        if hamming_distance(suffix_pattern, s) < d:
            for x in unique_letters:
                neigbourhood.add(x + s)
        else:
            neigbourhood.add(pattern[0] + s)
    return(neigbourhood)
    

def motif_enumeration(dna, k, d):
    patterns = set()
    dna_len = len(dna)
    for strand in dna:
        for i in range(0, len(strand) - k + 1):
            pattern = strand[i:i+k]
            neigbourhood = neigbours(pattern, d)

            for j in neigbourhood:
                freq = [0] * dna_len
                for l in dna:
                    freq_idx = dna.index(l)
                    for m in range(0, len(l) - k + 1):
                        pattern_strand = l[m:m+k]
                        if hamming_distance(j, pattern_strand) <= d:
                            freq[freq_idx] += 1
            
                
                # that is, the pattern exists in every dna
                if all(s >= 0 for s in freq):
                    patterns.add(j)
    return(patterns)

dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
k = 3
d = 1
motif_enumeration(dna, k, d)
for x in dna:
    print(x)