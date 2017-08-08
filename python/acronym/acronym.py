def abbreviate(s):
    import re
    l = re.compile('\w+').findall(s)
    return ''.join([x[0].upper() for x in l])
