from sympy import symbols
from math import sqrt

x = symbols('x')
f = 4 * x - 1.8 * x ** 2 + 1.2 * x ** 3 - 0.3 * x ** 4
print("This program solves {} using golden-section search algorithm".format(f))
iter = int(input("Input num of iteration: "))
xu = int(input("Input initial value xu: "))
xl = int(input("Input initial value xi: "))
e = float(input("Input stopping criterion: "))
g = (sqrt(5) - 1) / 2
print("{:<30}{:<30}{:<30}{:<30}{:<30}{:<30}{:<30}".format("Iteration", "x1", "x2", "xl", "xu",
                                                                "fx1", "fx2"))
for i in range(iter):
    d = g * (xu - xl)
    x1 = xl + d
    x2 = xu - d
    fx1 = f.subs(x, x1)
    fx2 = f.subs(x, x2)

    print("{:<30}{:<30}{:<30}{:<30}{:<30}{:<30}{:<30}".format("{}".format(i + 1), "{}".format(x1),
                                                              "{}".format(x2), "{}".format(xl), "{}".format(xu),
                                                              "{}".format(fx1),
                                                              "{}".format(fx2)))
    if fx1 > fx2:
        xl = x2
        xo = x1
    else:
        xu = x1
        xo = x2
    err = (1 - g) * (abs((xu - xl) / xo))
    print("Error: {}\n\n".format(err))
    if err > e:
        continue
    else:
        break
