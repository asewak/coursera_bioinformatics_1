# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:52:44 2018

@author: Ainesh.Sewak
"""


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


def pattern_to_number(pattern):
    
    unique_letters = 'ACGT'
    if pattern == '':
        return(0)
    # only last symbol
    symbol = pattern[-1]
    # last symbol removed
    prefix = pattern[:-1]
    out = 4 * pattern_to_number(prefix) + unique_letters.index(symbol)
    return(out)


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
    
    


def computing_frequencies_with_mismatches_reverse_complements(text, k, d):
    frequent_words = set()
    frequency_array = [0] * 4**k
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        pattern_rev = reverse_complement(pattern)
        
        neigbourhood = neigbours(pattern, d)
        neigbourhood_rev = neigbours(pattern_rev, d)
        
        for approximate_pattern in neigbourhood:
            j = pattern_to_number(approximate_pattern)
            frequency_array[j] += 1

        for approximate_pattern in neigbourhood_rev:
            j = pattern_to_number(approximate_pattern)
            frequency_array[j] += 1

    frequency_max = max(frequency_array)
    max_idx = [i for i, x in enumerate(frequency_array) if x == frequency_max]
    for i in max_idx:
        frequent_words.add(number_to_pattern(i,k))
    
    return(frequent_words)


text = 'CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT'
k = 9
d = 3



with open('C:/Users/ainesh.sewak/Downloads/dataset_9_8.txt') as f:
    file = f.read().splitlines()

text = file[0]
k = int(file[1].split()[0])
d = int(file[1].split()[1])

freq_with_mismatches_rev_complement = computing_frequencies_with_mismatches_reverse_complements(text, k, d)
print(' '.join(map(str,freq_with_mismatches_rev_complement)))






