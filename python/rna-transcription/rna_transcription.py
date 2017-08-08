def to_rna(s):
    l=[]
    for i in s:
        if i == 'G':
            l.append('C')
        elif i == 'C':
            l.append('G')
        elif i == 'T':
            l.append('A')
        elif i == 'A':
            l.append('U')
        else:
            return ''
    return ''.join(l)
    pass

