from factors import factors
def isPrime(n):
    return factors(n) == [1,n]