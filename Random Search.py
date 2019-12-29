import random
from sympy import symbols
import matplotlib.pyplot as plt
import numpy as np


x, y = symbols('x y')
f = -(3.5 * x + 2 * y + x ** 2 - x ** 4 - 2 * x * y - y ** 2)  # function to search for min
iter = int(input("Input iteration: "))
res = []
resx, resy, resmin, resiter = [], [], [], []
i = 0
for _ in range(iter):
    rx = random.uniform(-2.0, 2.0)
    ry = random.uniform(-2.0, 2.0)
    fxy = f.subs([(x, rx), (y, ry)])
    # First value must be stored
    resx.append(rx)
    resy.append(ry)
    res.append(fxy)
    
min = res[0]
resiter.append(0)
resmin.append(min)
for k in range(len(res)):
    # Find only min values in the list
    if min > res[k]:
        min = res[k]
        resmin.append(res[k])
        solx = resx[k]
        soly = resy[k]
        resiter.append(k)
for r in res:
    print("{}".format(r))
print("Min lists:")
for m in resmin:
    print("{}".format(m))
plt.plot(np.linspace(0, len(res), len(res), True), res)
plt.plot(resiter, resmin, label="Decreasing Values", color="red")
plt.xlabel("Iterations")
plt.ylabel("Values")
plt.title("Iteration and value")
plt.legend()
print("Min value: {} at x = {}, y = {}".format(min, solx, soly))
plt.show()




