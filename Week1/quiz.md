# Week 1 Quiz

## All questions carry equal weightage. All Python code is assumed to be executed using Python3. You may submit as many times as you like within the deadline. Your final submission will be graded.

# Note:

- If the question asks about a value of type string, remember to enclose your answer in single or double quotes.
- If the question asks about a value of type list, remember to enclose your answer in square brackets and use commas to separate list items.

## What does h(27993) return for the following function definition?

```bash
 def h(x):
    (d,n) = (1,0)
    while d <= x:
        (d,n) = (d*3,n+1)
    return(n) 
```

### 10

Feedback:

The function computes the smallest power of 3 that is bigger than x. Effectively, it computes the number of digits in the base 3 representation of x.

Accepted Answers:

(Type: Numeric) 10

2.5 points


## What is g(60) - g(48), given the definition of g below?

```bash
def g(n): 
    s=0
    for i in range(2,n):
        if n%i == 0:
           s = s+1
    return(s)
```

### 2

Feedback:

g(n) counts the number of factors of n, excluding 1 and n.

Accepted Answers:

(Type: Numeric) 2

2.5 points

## Consider the following function f.

```bash
def f(n): 
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           s = 1
    return(s%2 == 1)
```

## The function f(n) given above returns True for a positive number n if and only if:

 - n is an odd number.
 - is a prime number.
 - n is a perfect square. (correct)
 - n is a composite number.

Feedback:
f(n) sets s to 1 if there is a number i such that i*i == n.

Accepted Answers:

n is a perfect square.

## Consider the following function foo.

```bash
def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))
```

## Which of the following is correct?

 - The function always terminates with foo(n) = factorial of n
 - The function always terminates with foo(n) = n(n+1)/2
 - The function terminates for non­negative n with foo(n) = factorial of n
 - The function terminates for non­negative n with foo(n) = n(n+1)/2 (correct)

Feedback:

If m is negative, the function does not terminate. Otherwise, it computes 1+2+..+m = m(m+1)/2.

Accepted Answers:

The function terminates for non­negative n with foo(n) = n(n+1)/2