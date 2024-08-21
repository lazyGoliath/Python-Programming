def factors(x):
    factorsList = [1]
    for i in range(2,x+1):
        if(x%i == 0):
            factorsList += [i]
    return factorsList