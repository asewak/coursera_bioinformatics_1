# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 17:37:35 2018

@author: Ainesh.Sewak
"""

  
import itertools
import random


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

            
    
def _motifs(dna, k, profile):
    motifs = []
    for motif in dna:
        motifs.append(most_probable_kmer(motif, k, profile))
    return(motifs)


p = [0.1, 0.2, 0.3]

def random_p (p):
    s = sum(p)
    pr = [y/s for y in p]
    cum_pr = list(accumulate(pr))
    
    rand = random.random()
    
    for i in range(0, len(cum_pr)):
        if i == 0:
            if 0 <= rand < cum_pr[i]:
                val = i
        else:
            if cum_pr[i-1] <= rand < cum_pr[i]:
                val = i

    return(val)

dna = ['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
text = dna[0]
k = 8

motifs = []
for s in dna:
    rand = random.randint(0,len(dna[0]) - k)
    motifs.append(s[rand:(rand + k)])
profile = motifs_to_profile(motifs)

def profile_randomly_generated_kmer(text, k, profile):
    for i in range(0, len(text) - k + 1):
        pr = 



def randomized_motif_search(dna, k, t, n):
    motifs = []
    for s in dna:
        rand = random.randint(0,len(dna[0]) - k)
        motifs.append(s[rand:(rand + k)])
    best_motifs = motifs
        

    # strictly decreasing function, once it stops decreasing i.e. gets to 0 or just stops decreasing
    # the function will stop
    while True:
        profile = motifs_to_profile(motifs)
        
        # given this profile, find the the most probable motif matrix in dna, then iterate
        motifs = _motifs(dna, k, profile)

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return(best_motifs)