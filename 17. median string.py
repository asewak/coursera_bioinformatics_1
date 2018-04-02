# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 20:20:58 2018

@author: Ainesh
"""

def number_to_pattern(index, k):
    unique_letters = 'ACGT'
    if k == 1:
        return(unique_letters[index])
    prefix_index = index // 4
    r = index % 4
    symbol = unique_letters[r]
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    out = prefix_pattern + symbol
    return(out)

def hamming_distance(p, q):
    out = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            out += 1
    return(out)

#pattern = 'AAA'
#dna_i = 'GACGACCACGTT'
#dna = ['TTACCTTAAC','GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']



def min_distance_string(pattern, dna_i):
    
    k = len(pattern)
    len_dna_i = len(dna_i)
    hd_min = float("inf")
    
    for i in range(0, len_dna_i - k + 1):
        pattern_p = dna_i[i:i+k]
        hd_p = hamming_distance(pattern, pattern_p)
        if hd_p < hd_min:
            hd_min = hd_p
            #motif_min = pattern_p
    
    return(hd_min)

#min_distance_string(pattern, dna_i)

def min_distance_dna(pattern, dna):
    
    score = 0
    for dna_i in dna:
        score += min_distance_string(pattern, dna_i)
    
    return(score)
        
#min_distance_dna('AAA', dna)

def median_string(dna, k):
    
    frequency_array = [0] * 4**k
    frequency_array_len = len(frequency_array)
    score_min = float("inf")
    
    for i in range(0, frequency_array_len):
        pattern = number_to_pattern(i, k)
        score_p = min_distance_dna(pattern, dna)
        if score_p < score_min:
            score_min = score_p
            motif_min_num = i
    
    return(number_to_pattern(motif_min_num, k))

        
#dna = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTTCGGGACAG']        
#k = 3

#extra data set
#dna = ['TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT', 'CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA', 'TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT', 'TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA', 'ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG', 'TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA', 'TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC', 'GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA', 'CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG', 'CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG']
#k = 6

#quiz
dna = ['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC', 'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC', 'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG']
k = 7

median_string(dna, k)


with open('C:/Users/Ainesh/Downloads/dataset_158_9.txt') as f:
    file = f.read().splitlines()

k = int(file[0])
dna = file[1:]

kmer_min = median_string(dna, k)
print(kmer_min)

