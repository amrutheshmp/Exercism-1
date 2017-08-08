def is_isogram(s):
    s=s.lower()
    l = []
    for i in s:
        if i.isalpha() :
            l.append(i)
    l = sorted(l)            
    for i in range(0,len(l)-1):
        if(l[i]==l[i+1]):
            return False
    return True       
    pass
