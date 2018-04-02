# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:55:14 2018

@author: Ainesh
"""

import itertools

# sample input
#text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
#k = 5
#profile = {
#
#    'A': [0.2, 0.2, 0.3, 0.2, 0.3],
#    'C': [0.4, 0.3, 0.1, 0.5, 0.1],
#    'G': [0.3, 0.3, 0.5, 0.2, 0.4],
#    'T': [0.1, 0.2, 0.1, 0.1, 0.2]
#}

#extra data set
text = 'TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCCTGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGCGCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCACCCCTA'
k = 6
profile_str = '0.364 0.333 0.303 0.212 0.121 0.242\n0.182 0.182 0.212 0.303 0.182 0.303\n0.121 0.303 0.182 0.273 0.333 0.303\n0.333 0.182 0.303 0.212 0.364 0.152'

profile_split = profile_str.splitlines()


def profile_from_text(profile_split):
    # nested list comprehension loop to iterate and convert
    # the values of the lists to floats
    profile_list = [[float(x) for x in rec.split()] for rec in profile_split]
        
    # mapping the nucleotides list to each of their relevant profiles
    nucleotides = ['A', 'C', 'G', 'T']
    profile = dict(itertools.zip_longest(nucleotides, profile_list, fillvalue=None))
    return(profile)


def pr_profile(kmer, k, profile):
    
    pr = 1
    for i in range(0, k):
        pr *= profile[kmer[i]][i]
        
    return(pr)

def most_probable_kmer(text, k, profile):
    
    text_len = len(text)
    pr_max = 0
    
    for i in range(0, text_len - k + 1):
        kmer = text[i:i+k]
        pr_kmer = pr_profile(kmer, k, profile)
        if pr_kmer > pr_max:
            pr_max = pr_kmer
            kmer_max = kmer
    
    return(kmer_max)

    

with open('C:/Users/Ainesh/Downloads/dataset_159_3.txt') as f:
    file = f.read().splitlines()

text = file[0]
k = int(file[1])
profile = profile_from_text(file[2:])


most_probable_kmer(text, k, profile)