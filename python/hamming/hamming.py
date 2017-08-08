def distance(s1,s2):
    h = 0
    if len(s1) != len(s2):
        raise ValueError
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            h = h +1
    return h
    pass
