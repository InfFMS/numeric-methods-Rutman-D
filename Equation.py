import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.cos(x)

x = np.linspace(1, 0, 1000)
y = f(x)
l = 0
i = 0.1

while i <= 3.14:
    l += np.sqrt((f(i-0.1) - f(i))**2 + 0.1**2)
    i += 0.1
    #print(l, np.sqrt((f(i-0.1) - f(i))**2 + 0.1**2))
print("1:", l)


########################################################################################

def f(x):
    return np.cos(x) + 0.1*x**2


x = np.linspace(0, 3.14, 1000)
y = f(x)
l = 0
i = 0.1

while i <= 3.14:
    l += np.sqrt((f(i-0.1) - f(i))**2 + 0.1**2)
    i += 0.1
    #print(l, np.sqrt((f(i-0.1) - f(i))**2 + 0.1**2))
print("2:", l)



##################################################################

def f(x):
    return -1 * np.tanh(x-np.pi/2)



x = np.linspace(0, 3.14, 1000)
y = f(x)
l = 0
i = 0.1

while i <= 3.14:
    l += np.sqrt((f(i-0.1) - f(i))**2 + 0.1**2)
    i += 0.1
    #print(l, np.sqrt((f(i-0.1) - f(i))**2 + 0.1**2))
print("3:", l)

plt.plot(x, y)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.show()

##################################################################

def f(x):
    return -0.2*(x - np.pi)**3 + 0.5*(x - np.pi)**2 + 1

x = np.linspace(0, 3.14, 1000)
y = f(x)
l = 0
i = 0.1

while i <= 3.14:
    l += np.sqrt((f(i-0.1) - f(i))**2 + 0.1**2)
    i += 0.1
    #print(l, np.sqrt((f(i-0.1) - f(i))**2 + 0.1**2))
print("4:", l)

# plt.plot(x, y)
# plt.xlabel("Ось X")
# plt.ylabel("Ось Y")
# plt.show()