def word_count(s):
    import re
    d = {}
    split = sorted(re.findall(r'[a-zA-Z0-9]+', s.lower()))
    d[split[0]] = 1
    for i in range(0, len(split) - 1):
        if split[i] == split[i + 1]:
            d[split[i]] = d[split[i]] + 1
        else:
            d[split[i + 1]] = 1
    return d
    pass
