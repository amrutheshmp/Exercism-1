def slices(s,n):
    if n > len(s) or n == 0:
        raise ValueError('Give a Meaningfull Input')
    return [list( [ int(s[j]) for j in range(i,i+n) ] ) for i in range(len(s)-n+1)]
