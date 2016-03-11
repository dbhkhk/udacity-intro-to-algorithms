import math

def naive(a,b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

print naive(4,5)

def russian(a,b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 ==1:
            z = z + y
        y = y << 1
        x = x >> 1
    return z
print russian(4,5)


def time(a):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a
    steps = 0
    # your code here
    steps = math.ceil(a) * 2 + 3
    return steps

print time(5)
