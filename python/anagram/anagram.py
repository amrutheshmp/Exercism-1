def detect_anagrams(s,l):
    anagrams = []
    for i in l:
        if sorted(list(s.lower()))==sorted(list(i.lower())) and  s.lower() != i.lower() and not i in anagrams  :
            anagrams.append(i)
    return anagrams


