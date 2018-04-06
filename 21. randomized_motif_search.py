# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 22:45:27 2018

@author: Ainesh
"""

import itertools
import random


k = 8
t = 5
dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

def hamming_distance(p, q):
    out = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            out += 1
    return(out)


def motifs_to_profile(motifs):
    motif_length = len(motifs[0])
    motif_counts = [[1 for x in range(motif_length)] for y in range(4)]

    for i in range(0, len(motifs)):
        motif = motifs[i]
        for j in range(0, motif_length):
            if motif[j] == 'A':
                motif_counts[0][j] += 1
            if motif[j] == 'C':
                motif_counts[1][j] += 1
            if motif[j] == 'G':
                motif_counts[2][j] += 1
            if motif[j] == 'T':
                motif_counts[3][j] += 1
    
    n = sum([item[0] for item in motif_counts])
    motif_profile = [[y/n for y in x] for x in motif_counts]
    
    nucleotides = ['A', 'C', 'G', 'T']
    profile = dict(itertools.zip_longest(nucleotides, motif_profile, fillvalue=None))        
    return(profile)


def pr_profile(kmer, k, profile):
    
    pr = 1
    for i in range(0, k):
        pr *= profile[kmer[i]][i]
        
    return(pr)

def most_probable_kmer(text, k, profile):
    
    text_len = len(text)
    pr_max = 0
    kmer_max = text[0:k]
    
    for i in range(0, text_len - k + 1):
        kmer = text[i:i+k]
        pr_kmer = pr_profile(kmer, k, profile)
        if pr_kmer > pr_max:
            pr_max = pr_kmer
            kmer_max = kmer
    
    return(kmer_max)

def consensus(motifs):
    x = motifs_to_profile(motifs)
    x_list = list(x.values())
    x_list_t = list(map(list, zip(*x_list)))
    
    consensus = ''
    for l in x_list_t:
        nucleotides = 'ACGT'
        idx = l.index(max(l))
        consensus = consensus + nucleotides[idx]
    return(consensus)


def score(motifs):
    score = 0
    c = consensus(motifs)
    for motif in motifs:
        score += hamming_distance(motif, c)
    return(score)

            

            
    
    
def randomized_motif_search(dna, k, t):
    best_motifs = []
    for s in dna:
        rand = random.randint(0,len(dna[0]) - k)
        best_motifs.append(s[rand:(rand + k)])
        profile = motifs_to_profile(best_motifs)

    # strictly decreasing function, once it stops decreasing i.e. gets to 0 or just stops decreasing
    # the function will stop
    while True:
        motifs = []
        for motif in dna:
            motifs.append(most_probable_kmer(motif, k, profile))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return(best_motifs)
        
        

def randomized_motif_search_simulation(dna, k, t):
    
#    score_min = score(randomized_motif_search(dna, k, t))
    score_min = float("inf")
    for i in range(0, 1000 + 1):
        rms = randomized_motif_search(dna, k, t)
        if score(rms) < score_min:
            score_min = score(rms)
            optimal_motifs = rms

    return(optimal_motifs)


with open('C:/Users/Ainesh/Downloads/dataset_161_5.txt') as f:
    file = f.read().splitlines()

k = int(file[0].split()[0])
t = int(file[0].split()[1])
dna = file[1:]


rand_motifs = randomized_motif_search_simulation(dna, k, t)
score(rand_motifs)
' '.join(map(str, rand_motifs))