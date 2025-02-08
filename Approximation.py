import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100, 100, 100)
y = x**3 - x + 1

def f(x):
    return x**3 - x + 1

a = -6
b = 4
c = (a+b)/2
while b - a > 0.0001:
    if f(a)*f(c) <= 0:
        b = c
    else:
        a = c
    c = (a + b) / 2
print("first:", c)

################################################################################

def f(x):
    return x**3 - x**2 - 9*x + 9

x = np.linspace(-5, 5, 100)
y = f(x)

a = -4
b = 2
c = (a+b)/2
while b - a > 0.0001:
    if f(a)*f(c) <= 0:
        b = c
    else:
        a = c
    c = (a + b) / 2

a = 1
b = 3
c1 = (a+b)/2
while b - a > 0.0001:
    if f(a)*f(c1) <= 0:
        b = c1
    else:
        a = c
    c1 = (a + b) / 2

a = -2
b = 4
c2 = (a+b)/2
while b - a > 0.0001:
    if f(a)*f(c2) <= 0:
        b = c2
    else:
        a = c
    c2 = (a + b) / 2
print("second:", c, c1, c2)

################################################################################

def f(x):
    return x**2 - np.e**x


x = np.linspace(-3, 3, 100)
y = f(x)

a = -2
b = 0
c = (a+b)/2
while b - a > 0.0001:
    if f(a)*f(c) <= 0:
        b = c
    else:
        a = c
    c = (a + b) / 2
print("third:", c)


################################################################################

def f(x):
    return 5*x - 6 * np.log(x) - 7


x = np.linspace(1, 10, 100)
y = f(x)

a = 1.8
b = 3
c = (a+b)/2
while b - a > 0.0001:
    if f(a)*f(c) <= 0:
        b = c
    else:
        a = c
    c = (a + b) / 2

a = 0.01
b = 1.3
c1 = (a+b)/2
while b - a > 0.0001:
    if f(a)*f(c1) <= 0:
        b = c1
    else:
        a = c1
    c1 = (a + b) / 2

print("fourth:", c, c1)


################################################################################

def f(x):
    return np.cos(x) + 2*x - 3


x = np.linspace(1, 10, 100)
y = f(x)

a = 0
b = 4
c = (a+b)/2
while b - a > 0.0001:
    if f(a)*f(c) <= 0:
        b = c
    else:
        a = c
    c = (a + b) / 2

print("fiveth:", c)

