import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return np.sin(2*x) + 1
def f2(x):
    return -0.2*x**2 + 0.5
def sq(m, n):
    s = 0
    i = m
    while i < n:
        s += 0.1*(np.abs(f1(i)-f2(i)))
        i+=0.1
    print(s)
def tr(m, n):
    s = 0
    i = m
    while i < n:
        s += 0.1 * (np.abs(f1(i) - f2(i)) + np.abs(f1(i+0.1) - f2(i+0.1)))/2
        i += 0.1
    print(s)

x = np.linspace(0, np.pi, 100)
y = f1(x)
y1 = f2(x)
sq(0, np.pi)
tr(0, np.pi)
plt.plot(x, y)
plt.plot(x, y1)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.show()
#######################################################################

def f1(x):
    return np.cos(x) + 1.2
def f2(x):
    return -0.5*x**2 + 0.7

x = np.linspace(-np.pi/2, np.pi/2, 100)
y = f1(x)
y1 = f2(x)
sq(-np.pi/2, np.pi/2)
tr(-np.pi/2, np.pi/2)
plt.plot(x, y)
plt.plot(x, y1)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.show()
#######################################################################

def f1(x):
    return np.e**(-(x+1)**2) + np.e**(-(x-1)**2) + 0.5
def f2(x):
    return -0.3*x**2

x = np.linspace(-2, 2, 100)
y = f1(x)
y1 = f2(x)
sq(-2, 2)
tr(-2, 2)
plt.plot(x, y)
plt.plot(x, y1)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.show()
#######################################################################

def f1(x):
    return np.e**(-x**2) + 1
def f2(x):
    return -0.3*x**3 + 0.5

x = np.linspace(-2, 2, 100)
y = f1(x)
y1 = f2(x)
sq(-2, 2)
tr(-2, 2)
plt.plot(x, y)
plt.plot(x, y1)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.show()

#######################################################################

def f1(x):
    return np.e**(-x**2) + 0.5
def f2(x):
    return -0.2*np.sin(3*x) - 0.5

x = np.linspace(-2, 2, 100)
y = f1(x)
y1 = f2(x)
sq(-2, 2)
tr(-2, 2)
plt.plot(x, y)
plt.plot(x, y1)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.show()