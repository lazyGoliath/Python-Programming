def square(x):
    return x*x
def isEven(x):
    return (x%2==0)

print([square(x) for x in range(100) if isEven(x)])