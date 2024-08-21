from Primes import isPrime
def nPrimes(n):
    (count, i, pList) = (0,0, [])
    while(i<n):
        if isPrime(i):
            (count,pList) = (count+1, pList+[i])
        i+=1
    return pList