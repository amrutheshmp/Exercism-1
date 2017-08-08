def decode(s):
     n = 0
     l = []
     i = 0
     print(s)
     while ( n <len(s)):
         if s[n].isdigit():
             while s[n].isdigit():
                 i = i + 1
                 n = n + 1
             l.append((s[n]*int(s[n-i:n])))
             n = n + 1
             i = 0
         else:
             l.append(s[n])
             n = n + 1
     return (''.join(l))
     pass
 

def encode(s):
    l = []
    n = 0
    i = 1
    while(n<len(s)):
      if  n == len(s)-1 or not s[n] == s[n+1]  :
          l.append(s[n])
          n = n + 1 
      else:
          while n<len(s)-1 and s[n] == s[n+1]:
              i = i + 1
              n = n + 1
          l.append(str(i))
          l.append(s[n])
          i = 1
          n = n +1
    return (''.join(l))
    pass


