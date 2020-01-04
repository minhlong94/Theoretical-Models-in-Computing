from math import log, pow
import matplotlib.pyplot as plt
from numpy import linspace


def f(x):
    return log(pow(x, 4)) - 0.7


def bisection(a, b, ite):
    x1 = a
    x2 = b
    for i in range(ite):
        xr = (x1 + x2) / 2
        if ((ite - 1) == i):
            return xr
        else:
            if (f(x1) * f(xr) < 0):
                x2 = xr
                return bisection(x1, x2, ite - 1)
            elif (f(x1) * f(xr) > 0):
                x1 = xr
                return bisection(x1, x2, ite - 1)
            else:
                return xr


def falseposition(a, b, ite):
    x1 = a
    x2 = b
    for i in range(ite):
        xr = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
        if ((ite - 1) == i):
            return xr
        else:
            if (f(xr) > 0):
                x2 = xr
                return falseposition(x1, x2, ite - 1)
            elif (f(xr) < 0):
                x1 = xr
                return falseposition(x1, x2, ite - 1)
            else:
                return xr


k = int(input("Input the desired iteration: \n"))
ansb = bisection(0.5, 2, k)
print("The answer for bisection is: Bi{}".format(ansb))
ansfp = falseposition(0.5, 2, k)
print("The answer for false position is: {}".format(ansfp))

x = linspace(-2, 2, 100)
y = []
for x0 in x:
    y.append(f(x0))
plt.plot(x, y)
plt.grid()
plt.show()
