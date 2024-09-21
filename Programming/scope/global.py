def f():
    global x
    y=x
    print(y)
    x = 22

x=7
f()
print(x)

# Output : 7 22

def f(x):
    y=x
    print(y)
    x = 22

x=7
f(x)
print(x)

# Output : 7 7