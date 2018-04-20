
patterns = ['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT']

with open('C:/Users/ainesh.sewak/Downloads/dataset_198_10.txt') as f:
    file = f.read().splitlines()

def suffix(kmer):
    return(kmer[1:])

def prefix(kmer):
    return(kmer[:-1])

def overlap_graph(patterns):
    
    overlap = {}
    patterns_search = patterns[:]
    for kmer in patterns:
        for pattern in patterns_search:
            if suffix(kmer) == prefix(pattern) and kmer != pattern:
                overlap[kmer] = pattern
                
    return(overlap)
    
overlap = overlap_graph(file)


out = '\n'.join(['{} -> {}'.format(k,v) for k,v in overlap.items()])

f = open('C:/Users/ainesh.sewak/Documents/Bio 2/dataset_198_10_soln.txt', 'w')
f.write(out)
f.close()

# a way to collapse dictionaries
