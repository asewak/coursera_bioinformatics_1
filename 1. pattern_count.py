# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:10:33 2018

@author: Ainesh.Sewak
"""

import re
import pandas as pd

with open('C:/Users/ainesh.sewak/Downloads/dataset_2_10.txt') as f:
    file = f.read().splitlines()

# Change to 0 and 1 when doing actual
text = file[0]
pattern = file[1]



# find all overlapping patterns in the string
def pattern_count(text, pattern):
    pattern_regex = '(?=' + pattern + ')'
    return(len(re.findall(pattern_regex, text)))
    
pattern_count(text, pattern)

k = int(file[1])

def frequent_words(text, k):
        
pattern_list = []
    #k = 4
for i in range(0, len(text) - k):
    pattern = text[i:i+k]
    count = pattern_count(text, pattern)
    pattern_list.append(dict([('pattern',pattern), ('count', count)]))


# remove duplicate (key,value) pairs
seen = set()
new_l = []
for d in pattern_list:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_l.append(d)
    #print(new_l)

count_df = pd.DataFrame(new_l)
count_df = count_df[['pattern', 'count']]
#count_df.sort_values(by=['count'], ascending = False)

max_val = count_df['count'].max()
max_patterns = count_df[count_df['count'] == max_val]
max_patterns.to_string(columns = ['pattern'], index = False).replace('\n', ' ')
