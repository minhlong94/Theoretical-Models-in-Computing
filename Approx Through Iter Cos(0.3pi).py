from math import factorial, cos, pi
import matplotlib.pyplot as plt

res = 0
x = 0.3*pi
prev = res
i = 0

xs = [1]
ys = [1]

while True:
    res += ((-1)**i)*(x**(2*i))/(factorial(2*i))
    if abs(res-prev) <= 1e-8:
        break
    ys.append(res)
    prev = res
    i += 1
    xs.append(i)
    print(res)

plt.plot([item - 1 for item in xs], ys, 'b', label='approx')
plt.plot([item - 1 for item in xs], [cos(x) for _ in xs], 'r', label='true value')
plt.legend()
plt.title("Approximation through iteration of cos(x) at x = 0.3*pi")
plt.xlabel("Iteration")
plt.ylabel("Value")
plt.show()