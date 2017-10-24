def word_count(s):
    mydict = {}
    word_lst = s.split(' ')
    for word in word_lst:
        if not word in mydict:
            mydict[word] = 1
        else:
            mydict[word]+=1
    return mydict
