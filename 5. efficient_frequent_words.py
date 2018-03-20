# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:49:56 2018

@author: Ainesh.Sewak
"""

import itertools

# 1. find the lexographic frequency array

text = 'AAGCAAAGGTGGG'
x = itertools.permutations(text, r = 2)

# you can do for and then list append
# or you can use list comprehension
#for i in x:
#    print(''.join(i))
unique_letters = 'ACGT'
x = itertools.product(unique_letters, repeat = 2)
kmer = ([''.join(i) for i in x])

pattern_list = []

for i in range(0, len(kmer)):
    pattern = kmer[i]
    count = pattern_count(text, pattern)
    pattern_list.append(dict([('pattern',pattern), ('count', count)]))

count_df = pd.DataFrame(pattern_list)
count_df = count_df[['pattern', 'count']]
return(count_df)

def computing_frequencies(text, k):
    unique_letters = 'ACGT'
    x = itertools.product(unique_letters, repeat = k)
    kmer = ([''.join(i) for i in x])
    pattern_list = []    
    for i in range(0, len(kmer)):
        pattern = kmer[i]
        count = pattern_count(text, pattern)
        pattern_list.append(dict([('pattern',pattern), ('count', count)]))
    frequencies = [ i['count'] for i in pattern_list ]
    out = ' '.join(map(str,frequencies))
    print(out)

    #count_df = pd.DataFrame(pattern_list)
    #count_df = count_df[['pattern', 'count']]
    #return(count_df)




with open('C:/Users/ainesh.sewak/Downloads/dataset_2994_5.txt') as f:
    file = f.read().splitlines()

text = file[0]
k = int(file[1])

computing_frequencies(text, k)