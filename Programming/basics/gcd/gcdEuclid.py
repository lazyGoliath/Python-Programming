# The algorithm is based on the below facts :
# If we subtract a smaller number from a larger one (we reduce a larger number),
# GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we
# end up with GCD.
# Now instead of subtraction, if we divide the larger number, the algorithm stops
# when we find the remainder 0.

def gcdEuclid(a,b):
    if(a == 0):
        return a;
    else:
        return gcdEuclid(b%a , a);

if __name__ == "__main__":
  a = 10
  b = 15
  print("gcdEuclid(", a, ",", b, ") = ", gcdEuclid(a, b))

  a = 35
  b = 10
  print("gcdEuclid(", a, ",", b, ") = ", gcdEuclid(a, b))

  a = 31
  b = 2
  print("gcdEuclid(", a, ",", b, ") = ", gcdEuclid(a, b))

# Time Complexity: O(Log min(a, b))
# Auxiliary Space: O(Log (min(a,b))