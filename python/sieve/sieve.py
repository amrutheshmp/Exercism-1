import math
def sieve(n):
   l = [x for x in range(2,n+1)]
   for i in range(2,math.floor(math.sqrt(n))+1):
       k = [x*i for x in range (2,n//i+1)]
       l = [x for x in l if x not in k]
   return l
