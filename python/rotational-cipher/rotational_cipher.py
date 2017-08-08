def rotate(s,rot):
    l = []
    for i in s:
        if i.isalpha() and i.islower():
            if ord(i)+rot > ord('z') :
                l.append(chr(ord(i)+rot-26))
            else:
                l.append(chr(ord(i)+rot))
        elif i.isalpha() and i.upper():
            if ord(i)+rot > ord('Z') :
                l.append(chr(ord(i)+rot-26))
            else:
                l.append(chr(ord(i)+rot))
        else:
            l.append(i)
    return ''.join(l)
