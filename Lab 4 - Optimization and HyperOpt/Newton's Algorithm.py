import sympy as s

x = s.Symbol('x')
f = 4*x - 1.8*(x**2) + 1.2*(x**3) - 0.3*(x**4)

iter = int(input("Input your number of iteration:\n"))
err = float(input("Input your relative error:\n"))
x0 = int(input("Input your initial guess:\n"))
print("The program now calculates {}  using Newton's Algorithm\n".format(f))
x_prime = s.diff(f, x)  # Differentiate
x_prime2 = s.diff(f, x, 2)  # Second diff

for i in range(iter):
    x1 = x0 - x_prime.subs(x, x0)/x_prime2.subs(x, x0)  # Newton-Raphson formula
    relaerr = s.Abs((x1-x0)/x1)
    print("Iteration #{}, New x value: {}, Max value: {}, Relative Approx Error:"
          " {}\n".format(i, x1, f.subs(x, x1), relaerr))
    if relaerr > err:
        x0 = x1
        continue
    else:
        break