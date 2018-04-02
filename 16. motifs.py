# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:53:41 2018

@author: Ainesh
"""

import math

motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]


motif_length = len(motif)
motif_counts = [[0 for x in range(4)] for y in range(motif_length)]
for i in range(0, len(motifs)):
    motif = motifs[i]
    for j in range(0, motif_length):
        if motif[j] == 'A':
            motif_counts[j][0] += 1
        if motif[j] == 'C':
            motif_counts[j][1] += 1
        if motif[j] == 'G':
            motif_counts[j][2] += 1
        if motif[j] == 'T':
            motif_counts[j][3] += 1


motif_profile = [[y/len(motifs) for y in x] for x in motif_counts]

score = 0
for dist in motif_profile:
    score += entropy(dist)

def entropy(distribution):
    H = 0
    for i in distribution:
        if i != 0:
            H += - i * math.log2(i)
    return(H)
    
distribution = [0.2, 0.1, 0.0, 0.7]


motif_counts[1][0] = 1