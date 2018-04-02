# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:43:52 2018

@author: Ainesh.Sewak
"""

#pattern to number

def pattern_to_number(pattern):
        
    k = len(pattern)
    unique_letters = 'ACGT'
    x = itertools.product(unique_letters, repeat = k)
    kmer = ([''.join(i) for i in x])
    print(kmer.index(pattern))
    
pattern_to_number('ATGCAA')

def number_to_pattern(index, k):

    unique_letters = 'ACGT'
    x = itertools.product(unique_letters, repeat = k)
    kmer = ([''.join(i) for i in x])
    print(kmer[index])
    
number_to_pattern(5437,7)
number_to_pattern(5437,8)


################ More efficient ################

pattern = 'CTTCTCACGTACAACAAAATC'
pattern[:-1]

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

with open('C:/Users/ainesh.sewak/Downloads/dataset_3010_2.txt') as f:
    file = f.read().splitlines()
pattern = file[0]
print(pattern_to_number(pattern))


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
    
with open('C:/Users/ainesh.sewak/Downloads/dataset_3010_5.txt') as f:
    file = f.read().splitlines()
index = int(file[0])
k = int(file[1])
print(number_to_pattern(index, k))







