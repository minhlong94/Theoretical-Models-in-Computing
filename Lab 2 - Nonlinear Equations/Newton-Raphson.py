import math as m


def fpx(x, y):
    return (x ** 2 - y) / (5 * y)


def fpy(x, y):
    return -m.pow(x, 2) + x + 0.75


def fnew1(x, y):
    return y + x ** 2 - x - 0.75


def fnew2(x, y):
    return y + 5 * x * y - x ** 2


def fnew1x(x, y):
    return 2 * x - 1


def fnew1y(x, y):
    return 1


def fnew2x(x, y):
    return 5 * y - 2 * x


def fnew2y(x, y):
    return 1 + 5 * x


def fxp_iter(x, y, ite):
    for i in range(ite):
        if ((ite - 1) == i):
            return ansfx(x, y)
        else:
            y = fpy(x, y)
            x = fpx(x, y)
            return fxp_iter(x, y, ite - 1)


def newtonraph(x0, y0, step):
    for i in range(step):
        if ((step - 1) == i):
            return "{} {}".format(x0, y0)
        else:
            x0 = x0 - (fnew1(x0, y0) * fnew2y(x0, y0) - fnew2(x0, y0) * fnew1y(x0, y0)) / (
                        fnew1x(x0, y0) * fnew2y(x0, y0) - fnew1y(x0, y0) * fnew2x(x0, y0))
            y0 = y0 - (fnew2(x0, y0) * fnew1x(x0, y0) - fnew1(x0, y0) * fnew2x(x0, y0)) / (
                        fnew1y(x0, y0) * fnew2y(x0, y0) - fnew1y(x0, y0) * fnew2x(x0, y0))
            return newtonraph(x0, y0, step - 1)


def ansfx(x, y):
    print("Iter x = {} , y = {}".format(x, y))


k = int(input("Input the desired iteration: \n"))
for i in range(k):
    fxp_iter(1.2, 1.2, i)

ansnew = newtonraph(1.2, 1.2, k)
print("\n\nNewton-Raphson roots are: {}".format(ansnew))
