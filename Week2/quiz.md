# Week 2 Quiz

## All questions carry equal weightage. All Python code is assumed to be executed using Python3. You may submit as many times as you like within the deadline. Your final submission will be graded.

# Note:

- If the question asks about a value of type string, remember to enclose your answer in single or double quotes.
- If the question asks about a value of type list, remember to enclose your answer in square brackets and use commas to separate list items.

## One of the following 10 statements generates an error. Which one? (Your answer should be a number between 1 and 10.)

```bash
x = [[3,5],"mimsy",2,"borogove",1]  # Statement 1
y = x[0:50]                          # Statement 2
z = y                                # Statement 3
w = x                                # Statement 4
x[1] = x[1][:5] + 'ery'              # Statement 5
y[1] = 4                             # Statement 6
w[1][:3] = 'fea'                     # Statement 7
z[4] = 42                            # Statement 8
x[0][0] = 5555                       # Statement 9
a = (x[3][1] == 1)                   # Statement 10
```

### 7

Feedback:
At statement 7, w[1] is the string "mimsy", which cannot be updated in place.

Accepted Answers:
(Type: Numeric) 7

## Consider the following lines of Python code.

```bash
b = [43,99,65,105,4]
a = b[2:]
d = b[1:]
c = b
d[1] = 95
b[2] = 47
c[3] = 73
```

## Which of the following holds at the end of this code?

 - a[0] == 47, b[3] == 73, c[3] == 73, d[1] == 47
 - a[0] == 65, b[3] == 105, c[3] == 73, d[1] == 95
 - a0] == 65, b[3] == 73, c[3] == 73, d[1] == 95 (correct)
 - a[0] == 95, b[3] == 73, c[3] == 73, d[1] == 95

Feedback:
a[0] == 65, b[3] == 73, c[3] == 73, d[1] == 95
b and c refer to the same list, while a and d are two independent slices. The update to d[1] does not affect any other list. The update to b[2] does not affect a or d. The update to c[3] is also reflected in b[3].

Accepted Answers:
a[0] == 65, b[3] == 73, c[3] == 73, d[1] == 95

## What is the value of endmsg after executing the following lines?

```bash
startmsg = "anaconda"
endmsg = ""
for i in range(1,1+len(startmsg)):
  endmsg = endmsg + startmsg[-i]
```

### "adnocana"

Feedback:
"adnocana"
The loop copies each letter in startmsg from right to left to the end of endmsg, so the resulting string is the reverse of the original string.

Accepted Answers:
(Type: Regex Match) \s*\'adnocana\'\s*
(Type: Regex Match) \s*\"adnocana\"\s*

## What is the value of mylist after the following lines are executed?

```bash
def mystery(l):
  l = l[2:]
  return(l)

mylist = [7,11,13,17,19,21]
mystery(mylist)
```

### [7,11,13,17,19,21] 

Feedback:
[7,11,13,17,19,21]
The update l = l[2:] inside the function creates a new list, so the list passed as the argument is not changed.

Accepted Answers:
(Type: Regex Match) \s*\[\s*7,\s*11,\s*13,\s*17,\s*19,\s*21\s*]\s*
