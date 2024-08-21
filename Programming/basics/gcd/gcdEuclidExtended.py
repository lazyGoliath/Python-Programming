#  Extended Euclidean algorithm also finds integer coefficients
#  x and y such that: ax + by = gcd(a, b) 

def gcdEuclidExtended():
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdEuclidExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


# Driver code
a, b = 35, 15
g, x, y = gcdEuclidExtended(a, b)
print("gcd(", a, ",", b, ") = ", g)