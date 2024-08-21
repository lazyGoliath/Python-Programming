def numSize(x):
    size = 0
    while x>0:
      x = x/10
      size += 1
    return size

def interverse(n):
    size = numSize(n)
    newNum = 0
    for i in range(1, size+1):
      newNum = (n%10)*10**(size-i) + newNum
      n = n/10
    return newNum

def matched(s):
  count = 0
  for i in range(0,len(s)):
    if count == 0 and s[i] == ")":
      return 0
    else:
      if s[i] == "(":
        count += 1
      elif(s[i] == ")"):
        count -= 1
      else:
        continue
  if count == 0:
   return 1
  else:
    return 0
  
def isPrime(x):
  count = 1
  for i in range(2,x+1):
    if x%i == 0:
      count += 1
    if count>2:
      return 0
  return 1

def sumprimes(list):
  sum = 0
  for num in list:
    if isPrime(num):
      sum += num
  return sum