from Primes import isPrime
def primesUptoN(x):
    primeList = []
    for i in range(1,x+1):
        if(isPrime(i)):
            primeList += [i]
    return primeList