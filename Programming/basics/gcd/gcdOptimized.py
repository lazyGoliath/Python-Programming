def gcdOptimized(m,n):
    # for f in range(min(m, n) + 1, 1):
    #     if(n % f == 0 and m % f == 0):
    #         return f;
    i = min(m,n);
    while(i>0):
        if(n % i == 0 and m % i == 0):
              return i;
        else:
             i -= 1;