def hey(s):
    import re
    if ''.join(re.findall(r'[a-zA-Z]',s)).isupper():
        return  "Whoa, chill out!"
    elif re.match(r'^.*\?\s*$',s):
        return "Sure."
    elif re.match(r'^\s*$',s):
        return "Fine. Be that way!"
    else :
        return "Whatever."
    pass



