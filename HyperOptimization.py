from hyperopt import fmin, tpe, hp
from sympy import symbols

x, y = symbols('x y')
f = - (3.5 * x + 2 * y + x ** 2 - x ** 4 - 2 * x * y - y ** 2)


def func(space):
    x = space['x']
    y = space['y']
    return -(3.5 * x + 2 * y + x ** 2 - x ** 4 - 2 * x * y - y ** 2)


# range to find x and y
space = {
    'x': hp.uniform('x', -10, 10),
    'y': hp.uniform('y', -10, 10)
}

iter = int(input("Input iterations: "))
best = fmin(
    fn=func,
    space=space,
    algo=tpe.suggest,
    max_evals=iter
)

print("Found minimum after {} trials:".format(iter))
print(best)
rx = best['x']
ry = best['y']
print("Min value of function: {}".format(f.subs([(x, rx), (y, ry)])))
