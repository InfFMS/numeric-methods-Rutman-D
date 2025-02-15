import matplotlib.pyplot as plt
import numpy as np

I = [0.1, 0.311, 0.522, 0.733, 0.944, 1.156, 1.367, 1.578, 1.789, 2.0]
U = [0.599, 1.528, 2.741, 3.971, 4.675, 5.731, 7.149, 8.042, 8.851, 10.109]

a = 0
b = 0

for i in range(0, len(I)):
    a += I[i]**2

for i in range(0, len(U)):
    b += 2*I[i]*U[i]

k = b/(2*a)
x = np.linspace(0, 2, 10)
y = k*x

print("R =", k)

plt.plot(x, y)
plt.scatter(I, U, color = "red")
plt.xlabel("I")
plt.ylabel("U")
plt.show()