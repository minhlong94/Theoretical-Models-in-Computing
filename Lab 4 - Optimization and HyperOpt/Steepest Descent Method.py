from sympy import diff, solve, Abs

x, y, h = s.symbols('x y h')
# f = (x - 3)**2 + (y - 2)**2   # Lab exercise
f = 2*x*y + 2*x - x**2 - 2*(y**2)  # TMC Optimization slide example
print("This program solves {} using Steepest Descent Method".format(f))
inix = int(input("Input initial value x: \n"))
iniy = int(input("Input initial value y: \n"))
e = round(float(input("Input stopping criteria: \n")), 10)
iter = int(input('Input number of iterations: \n'))

for i in range(iter):
    fx = diff(f, x)
    fy = diff(f, y)
    xh = inix + fx.subs({x: inix, y: iniy}) * h
    yh = iniy + fy.subs({x: inix, y: iniy}) * h
    gh = f.subs({x: xh, y: yh})  # Gradient Vector
    if gh != 0:
        print("{} Gradient Vector is: {}".format(i+1, gh))
        gh_prime = diff(gh, h)
        sol = solve(gh_prime, h)
        xhn = xh.subs(h, sol[0])
        yhn = yh.subs(h, sol[0])
        print("New x value: {}, New y value: {}\n".format(xhn, yhn))
        relaerrX = Abs((xhn-inix)/xhn)
        relaerrY = Abs((xhn-iniy)/xhn)
        relaerr = max(relaerrX, relaerrY)  # Max of two relative errors
        print("Error is: {}".format(relaerr))
        if relaerr > e:
            inix = xhn
            iniy = yhn
            continue
        else:
            break
    else:  # if the value converges
        print("New gradient vector is: {}".format(gh))
        print("Final value is: x = {}, y= {}".format(xhn, yhn))
        break
