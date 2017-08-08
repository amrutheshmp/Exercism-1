def encode(s):
    s=''.join([x.lower() for x in s if x.isalpha()or x.isdigit()])
    l = []
    key = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n', 'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'g', 'u':'f', 'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a' }
    for i in s:
        if i.isalpha():
            l.append(key[i])
        else:
            l.append(i)
    return ' '.join([''.join(l)[i:i+5] for i in range(0, len(l), 5)])
    
def decode(s):
    s=''.join([x.lower() for x in s if x.isalpha() or x.isdigit()])
    l = []
    key = {'z':'a','y':'b','x':'c','w':'d','v':'e','u':'f','t':'g','s':'h','r':'i','q':'j','p':'k','o':'l','n':'m','m':'n','l':'o','k':'p','j':'q','i':'r','h':'s','g':'t','f':'u','e':'v','d':'w','c':'x','b':'y','a':'z'}
    for i in s:
        if i.isalpha():
            l.append(key[i])
        else:
            l.append(i)
    return ''.join(l)
