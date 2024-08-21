# Algorithm to find GCD using Stein’s algorithm gcd(a, b) :
# 1.) If both a and b are 0, gcd is zero gcd(0, 0) = 0.
# 2.) gcd(a, 0) = a and gcd(0, b) = b because everything divides 0.
# 3.) If a and b are both even, gcd(a, b) = 2*gcd(a/2, b/2) because 2 is a common divisor.
# Multiplication with 2 can be done with bitwise shift operator.
# 4.) If a is even and b is odd, gcd(a, b) = gcd(a/2, b). Similarly, if a is odd and b is even, then 
# gcd(a, b) = gcd(a, b/2). It is because 2 is not a common divisor.
# 5.) If both a and b are odd, then gcd(a, b) = gcd(|a-b|/2, b). Note that difference of two odd
# numbers is even
# 6.) Repeat steps 3–5 until a = b, or until a = 0. In either case, the GCD is power(2, k) * b, where
# power(2, k) is 2 raise to the power of k and k is the number of common factors of 2 found in step 3.

#ITERATIVE APPROACH

def gcd(a, b):

	# GCD(0, b) == b; GCD(a, 0) == a,
	# GCD(0, 0) == 0
	if (a == 0):
		return b

	if (b == 0):
		return a

	# Finding K, where K is the
	# greatest power of 2 that
	# divides both a and b.
	k = 0

	while(((a | b) & 1) == 0):
		a = a >> 1
		b = b >> 1
		k = k + 1

	# Dividing a by 2 until a becomes odd
	while ((a & 1) == 0):
		a = a >> 1

	# From here on, 'a' is always odd.
	while(b != 0):

		# If b is even, remove all
		# factor of 2 in b
		while ((b & 1) == 0):
			b = b >> 1

		# Now a and b are both odd. Swap if
		# necessary so a <= b, then set
		# b = b - a (which is even).
		if (a > b):

			# Swap u and v.
			temp = a
			a = b
			b = temp

		b = (b - a)

	# restore common factors of 2
	return (a << k)

a = 34
b = 17

print("Gcd of given numbers is ", gcd(a, b))

# Time Complexity: O(N*N)
# Auxiliary Space: O(1)

# RECURSIVE APPROACH

def gcd(a, b):

	if (a == b):
		return a

	# GCD(0, b) == b; GCD(a, 0) == a,
	# GCD(0, 0) == 0
	if (a == 0):
		return b

	if (b == 0):
		return a

	# look for factors of 2
	# a is even
	if ((~a & 1) == 1):

		# b is odd
		if ((b & 1) == 1):
			return gcd(a >> 1, b)
		else:
			# both a and b are even
			return (gcd(a >> 1, b >> 1) << 1)

	# a is odd, b is even
	if ((~b & 1) == 1):
		return gcd(a, b >> 1)

	# reduce larger number
	if (a > b):
		return gcd((a - b) >> 1, b)

	return gcd((b - a) >> 1, a)

a, b = 34, 17
print("Gcd of given numbers is ",
	gcd(a, b))

# Time Complexity: O(N*N) where N is the number of bits in the larger number.
# Auxiliary Space: O(N*N) where N is the number of bits in the larger number.