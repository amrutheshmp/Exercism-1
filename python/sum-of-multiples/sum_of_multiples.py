def sum_of_multiples(n,l):
    sum = {0}
    result = 0
    m = 1
    for i in l:
        while(i*m < n):
            sum.add(i*m)
            m = m + 1
        m = 1
    for i in sum :
       result = i + result
    return result
