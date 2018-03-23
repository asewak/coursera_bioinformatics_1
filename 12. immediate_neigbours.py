


def hamming_distance(p, q):
    out = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            out += 1
    return(out)

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
                


with open('C:/Users/Ainesh/Downloads/dataset_3014_4 (2).txt') as f:
    file = f.read().splitlines()

pattern = file[0]
d = int(file[1])

pattern = 'GGCCCAGAG'
d = 3

out = neigbours(pattern, d)

out_patterns = '\n'.join(map(str,out))

with open('C:/Users/Ainesh/Downloads/dataset_3014_4 (2)_out.txt', 'w') as f:
    f.write(out_patterns)
                
                
                
                
                
                
                
                