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
        return([pattern])
    if len(pattern) == 1:
        return(['A', 'C', 'G', 'T'])
    neigbourhood = []
    suffix_pattern = pattern[1:]
    suffix_neigbours = neigbours(suffix_pattern, d)
    for s in suffix_neigbours:
        if hamming_distance(suffix_pattern, s) < d:
            for x in unique_letters:
                neigbourhood.append(x + s)
        else:
            neigbourhood.append(pattern[0] + s)
    return(neigbourhood)

            

def motif_enumeration(dna, k, d):
    patterns = set()
    #dna_len = len(dna)
    for strand in dna:
        for i in range(0, len(strand) - k + 1):
            pattern = strand[i:i+k]
            neigbourhood = neigbours(pattern, d)

            for j in neigbourhood:
                #freq = [0] * dna_len
                #c = 0
                pattern_appears = True
                for l in dna:
                    match_in_dna = False
                    #freq_idx = dna.index(l)
                    for m in range(0, len(l) - k + 1):
                        pattern_strand = l[m:m+k]
                        if hamming_distance(j, pattern_strand) <= d:
                            #freq[freq_idx] += 1
                            #c += 1
                            match_in_dna = True
                            break
                    if match_in_dna == False:
                        pattern_appears = False
                        break
                # that is, the pattern exists in every dna strand
                #if all(s > 0 for s in freq):
                #if c == len(dna):
                if pattern_appears:
                    patterns.add(j)
    return(patterns)


with open('C:/Users/ainesh.sewak/Downloads/dataset_156_8.txt') as f:
    file = f.read().splitlines()



dna = file[1:]
k = int(file[0].split()[0])
d = int(file[0].split()[1])

motifs = motif_enumeration(dna, k, d)
print(' '.join(map(str,motifs)))




