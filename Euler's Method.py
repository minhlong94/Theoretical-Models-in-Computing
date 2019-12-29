from sympy import symbols

x, y = symbols("x, y")
df = -2*x**3 + 12*x**2 - 20*x + 8.5  # diff equation that uses Euler's method
ftrue = -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1  # True function to compare results
a = int(input("Input left range: "))  # a
b = int(input("Input right range: "))  # b
n = int(input("Input number of intervals: "))  # number of intervals
f0 = float(input("Input initial value of f: "))  # initial value of function at x = a
h = (b-a)/n  # Step (or k/n where k = 0,1,2,...n
print("{:<20}{:<20}{:<20}".format("x value", "Euler's value", "True value"))
for i in range(n):
    f = f0 + df.subs(x, a+h*i)*h  # Euler's method
    freal = ftrue.subs(x, a+h*i)  # Real value to compare
    print("{:<20}{:<20}{:<20}".format("{}".format(a+h*i), "{}".format(f), "{}".format(freal)))
    f0 = f  # Next iteration uses the previous result

