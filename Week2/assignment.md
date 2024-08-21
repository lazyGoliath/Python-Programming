# Week 2 Programming Assignment

- Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
- You may define additional auxiliary functions as needed.
- In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
- For each function, there are normally some public test cases and some (hidden) private test cases.
- "Compile and run" will evaluate your submission against the public test cases.
- "Submit" will evaluate your submission against the hidden private test cases. There are 10 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
- Ignore warnings about "Presentation errors".

## Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n. 
## Here are some examples of how your function should work.

```bash
>>> intreverse(783)
387
>>> intreverse(242789)
987242
>>> intreverse(3)
3
```

### Solution :

```python
def intreverse(n):
  ans = 0
  while n > 0:
    (d,n) = (n%10,n//10)
    ans = 10*ans + d
  return(ans)
```

## Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.
## Here are some examples to show how your function should work.

```bash 
>>> matched("zb%78")
True
>>> matched("(7)(a")
False
>>> matched("a)*(?")
False
>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True
```

### Solution :

```python
def matched(s):
  nested = 0
  for i in range(0,len(s)):
    if s[i] == "(":
       nested = nested+1
    elif s[i] == ")":
       nested = nested-1
       if nested < 0:
          return(False)    
  return(nested == 0)
```

## Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.
## Here are some examples to show how your function should work.

```bash
>>> sumprimes([3,3,1,13])
19
>>> sumprimes([2,4,6,9,11])
13
>>> sumprimes([-3,1,6])
0
```

### Solution :

```python
def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist = factorlist + [i]
  return(factorlist)

def isprime(n):
  return(factors(n) == [1,n])


def sumprimes(l):
  sum = 0
  for i in range(0,len(l)):
    if isprime(l[i]):
      sum = sum+l[i]
  return(sum)
```

## Private Test cases used for evaluation	Input	Expected Output	Actual Output	Status

- Test Case 1	
```bash
intreverse(31511)
 11513
11513\n
Passed
```

- Test Case 2	
```bash
intreverse(4)
 4
4\n
Passed
```

- Test Case 3	
```bash
intreverse(15135324234235)
 53243242353151
53243242353151\n
Passed
```

- Test Case 4	
```bash
matched("a3qw3;4w3(aasdgsd)((agadsgdsgag)agaga)")
 True
True\n
Passed
```

- Test Case 5	
```bash
matched("(ag(Gaga(agag)Gaga)GG)a)33)cc(")
 False
False\n
Passed
```

- Test Case 6	
```bash
matched("(adsgdsg(agaga)a")
 False
False\n
Passed
```

- Test Case 7	
```bash
matched("15ababa.agaga[][[[")
 True
True\n
Passed
```

- Test Case 8	
```bash
sumprimes([101,93,97,44])
 198
198\n
Passed
```

- Test Case 9	
```bash
sumprimes([1001,393,743,59])
 802
802\n
Passed
```

- Test Case 10	
```bash
sumprimes([11,11,11,13,11,-11])
 57
57\n
Passed
```

10 out of 10 tests passed.
You scored 100.0/100.

## Driver Code :

```python
import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "intreverse":
   arg = parse(farg)
   print(intreverse(arg))
elif fname == "matched":
   arg = parse(farg)
   print(matched(arg))
elif fname == "sumprimes":
   arg = parse(farg)
   print(sumprimes(arg))
else:
   print("Function", fname, "unknown")
```