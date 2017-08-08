def is_pangram(s):
    s=s.lower()
    l=[]
    for i in s:
        if i.isalpha():
            l.append(i)
    l=sorted(list(set(l)))
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if alphabets == l:
        return True
    else:
        return False

is_pangram('The hhdhdhdh')
