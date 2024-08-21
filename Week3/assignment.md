# Week 3 Programming Assignment

- Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
- You may define additional auxiliary functions as needed.
- In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
- For each function, there are normally some public test cases and some (hidden) private test cases.
- "Compile and run" will evaluate your submission against the public test cases.
- "Submit" will evaluate your submission against the hidden private test cases. There are 10 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
- Ignore warnings about "Presentation errors".

## Write a function contracting(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly decreases.
## Here are some examples of how your function should work.

```bash
  >>> contracting([9,2,7,3,1])
  True

  >>> contracting([-2,3,7,2,-1]) 
  False

  >>> contracting([10,7,4,1])
  False
```

### Solution :

```python
def contracting(l):
  if len(l) < 3:
    return True
  for i in range(1, len(l) - 1):
    if abs(l[i+1] - l[i]) >= abs(l[i] - l[i-1]):
      return False
  return True
```

## In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than its neighbours and a valley if it is strictly less than its neighbours. Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] where hc is the number of hills in l and vc is the number of valleys in l.
## Here are some examples to show how your function should work.

```bash 
 
>>> counthv([1,2,1,2,3,2,1])
[2, 1]

>>> counthv([1,2,3,1])
[1, 0]

>>> counthv([3,1,2,3])
[0, 1]

```

### Solution :

```python
def counthv(l):
  num_hills = num_valleys = 0
  for i in range(1,len(l)-1):
    if(l[i]>l[i-1] and l[i]>l[i+1]):
      num_hills += 1
    elif l[i]<l[i-1] and l[i]<l[i+1]:
      num_valleys += 1
  return [num_hills, num_valleys]
```

## A square n×n matrix of integers can be written in Python as a list with n elements, where each element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix:
```bash
  1  2  3
  4  5  6
  7  8  9
```
## would be represented as [[1,2,3], [4,5,6], [7,8,9]].

## Write a function leftrotate(m) that takes a list representation m of a square matrix as input, and returns the matrix obtained by rotating the original matrix counterclockwize by 90 degrees. For instance, if we rotate the matrix above, we get
```bash
  3  6  9
  2  5  8    
  1  4  7
```
## Your function should not modify the argument m provided to the function rotate().
## Here are some examples to show how your function should work.

```bash
 >>> leftrotate([[1,2],[3,4]])
  [[2, 4], [1, 3]]

  >>> leftrotate([[1,2,3],[4,5,6],[7,8,9]])
  [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

  >>> leftrotate([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

### Solution :

```python
def leftrotate(m):
  if len(m) != len(m[0]):
    raise ValueError("Input matrix must be square")
  n = len(m)
  rotated = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      rotated[n -1 -j][i] = m[i][j]
  return rotated
```

## Private Test cases used for evaluation	Input	Expected Output	Actual Output	Status

- Test Case 1	
```bash
contracting([98,21,77,35,11])
 True
True\n
Passed
```

- Test Case 2	
```bash
contracting([-36,25,79,38,11])
 True
True\n
Passed
```

- Test Case 3	
```bash
contracting([100,77,33,11])
 False
False\n
Passed
```

- Test Case 4	
```bash
contracting([12,-11,10,-9,8,-7,6,-5,4,-3,2,-1])
 True
True\n
Passed
```

- Test Case 5	
```bash
contracting([-32,-11,10,-9,8,-7,6,-5,4,-3,2,-1])
 False
False\n
Passed
```

- Test Case 6	
```bash
counthv([23,44,22,1,26,10])
 [2, 1]
[2, 1]\n
Passed
```

- Test Case 7	
```bash
counthv([23,44,22,1,5,1])
 [2, 1]
[2, 1]\n
Passed
```

- Test Case 8	
```bash
counthv([1,10,2,11,3,12,4,13,5,14,6])
 [5, 4]
[5, 4]\n
Passed
```

- Test Case 9	
```bash
counthv([1,10,2,11,3,12,4,13,5,14,23])
 [4, 4]
[4, 4]\n
Passed
```

- Test Case 10	
```bash
counthv([12,55,22,88,40])
 [2, 1]
[2, 1]\n
Passed
```

- Test Case 11	
```bash
leftrotate([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
 [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]\n
Passed
```

- Test Case 12	
```bash
leftrotate([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]])
 [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]\n
Passed
```

- Test Case 13	
```bash

leftrotate([[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3],[4,4,4,4,4,4],[5,5,5,5,5,5],[6,6,6,6,6,6]])
 [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]\n
Passed
```

- Test Case 14	
```bash

leftrotate([[1,1,1,1,1,1,1],[2,2,2,2,2,2,2],[3,3,3,3,3,3,3],[4,4,4,4,4,4,4],[5,5,5,5,5,5,5], [6,6,6,6,6,6,6], [7,7,7,7,7,7,7]])
 [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]
[[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]\n
Passed
```

- Test Case 15	
```bash
leftrotate([[1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5], [6,6,6,6,6,6,6,6], [7,7,7,7,7,7,7,7], [8,8,8,8,8,8,8,8]])
 [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]
[[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]\n
Passed
```

15 out of 15 tests passed.
You scored 100.0/100.

## Driver Code :

```python
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "contracting":
  arg = parse(farg)
  print(contracting(arg))

if fname == "counthv":
  arg = parse(farg)
  print(counthv(arg))

if fname == "leftrotate":
  arg = parse(farg)
  savearg = arg
  ans = leftrotate(arg)
  if savearg == arg:
    print(ans)
  else:
    print("Side effect")
```