from sympy import symbols
from math import exp, factorial


def taylor(function, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x, i).subs(x, x0)) / (factorial(i)) * (x - x0) ** i
        i += 1
    return p


x = symbols('x')
expo = exp(1)
f = (x ** 4) * (expo ** (-3 * (x ** 2)))  # function
print("Taylor approximation of {}".format(f))
x0 = float(input("Input Taylor's center: "))
i = int(input("Input Taylor's order: "))
funcfinal = taylor(f, x0, i)
print("{}-th order Taylor approx: \n{}".format(i, funcfinal))
xn = float(input("Input value x: "))
res = funcfinal.subs(x, xn)
print(res)
