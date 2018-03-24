# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:02:28 2018

@author: Ainesh.Sewak
"""

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
    

def approximate_pattern_count(pattern, text, d):
    approximate_pattern_frequency = 0
    pattern_length = len(pattern)
    for i in range(0, len(text) - pattern_length + 1):
        pattern_in_text = text[ i : i + pattern_length]
        hd_pattern = hamming_distance(pattern, pattern_in_text)
        if hd_pattern <= d:
            approximate_pattern_frequency += 1
    
    return(approximate_pattern_frequency)
    
    
    
def immediate_neigbours(pattern):
    
    unique_letters = 'ACGT'
    neigbourhood = set()
    neigbourhood.add(pattern)
    for i in range(0, len(pattern)):
        symbol = pattern[i]
        for x in unique_letters.replace(symbol, ''):
            neigbour = pattern[:i] + x + pattern[i+1:]
            neigbourhood.add(neigbour)
    return(neigbourhood)

    
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
                
    

def iterative_neigbours(pattern, d):
    neigbourhood = set()
    neigbourhood.add(pattern)
    for i in range(0, d):
        # Using copy() will allow you to iterate over a copy of the set, while removing items from the original.
        for s in neigbourhood.copy():
            im_nbrs = immediate_neigbours(s)
            neigbourhood.update(im_nbrs)
    return(neigbourhood)



def computing_frequencies_with_mismatches(text, k, d):
    frequent_words = set()
    frequency_array = [0] * 4**k
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        neigbourhood = neigbours(pattern, d)
        for approximate_pattern in neigbourhood:
            j = pattern_to_number(approximate_pattern)
            frequency_array[j] += 1
    frequency_max = max(frequency_array)
    max_idx = [i for i, x in enumerate(frequency_array) if x == frequency_max]
    for i in max_idx:
        frequent_words.add(number_to_pattern(i,k))
    
    return(frequent_words)




    
def frequent_words_with_mismatches(text, k, d):
    kmer_counts = {}
    for i in range(0, len(text) - k + 1):
        kmer = text[i : i + k]
        if kmer not in kmer_counts:
            kmer_counts[kmer] = approximate_pattern_count(kmer, text, d)
    
    max_count = max(kmer_counts.values())
    
    frequent_words = []
    for kmer, count in kmer_counts.items():
        if count == max_count:
            frequent_words.append(kmer)
    
    return(frequent_words, kmer_counts)
    
text = 'CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC'
k = 10
d = 2


with open('C:/Users/ainesh.sewak/Downloads/dataset_9_7.txt') as f:
    file = f.read().splitlines()

text = file[0]
k = int(file[1].split()[0])
d = int(file[1].split()[1])

computing_frequencies_with_mismatches(text, k, d)