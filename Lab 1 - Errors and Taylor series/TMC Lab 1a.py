import matplotlib.pyplot as plt

# Important: I forgot what this code does.
def fac(n):
    t = 1
    for i in range(1, n + 1):
        t = t * i
    return t


k = 5
res = 1
res2 = 1
res2final = 1
tvalue = 6.737947 * (10 ** -3)
xs1 = [1]
xs2 = [1]
ys1 = [1]
ys2 = [1]

print("First approach: ")
print("{:<20}{:<20}{:<20}".format("TrueValue", "Error", "App Error"))
for i in range(1, 21):
    tempres = res
    if i % 2 == 0:
        res = res + (k ** i) / fac(i)
    else:
        res = res - (k ** i) / fac(i)
    terror = (tvalue - res) / tvalue
    aerror = (res - tempres) / res
    print("{:<20}{:<20}{:<20}".format("{}".format(round(res, 4)), "{}".format(round(terror, 4)), "{}".format(round(aerror, 4))))
    xs1.append(i)
    ys1.append(res)

plt.plot([item - 1 for item in xs1], [item - 1 for item in ys1])
plt.title("First Approach")
plt.xlabel("Terms")
plt.ylabel("Value")
plt.show()

print("\nSecond approach: ")
print("{:<20}{:<20}{:<20}".format("TrueValue", "Error", "App Error"))
for i in range(1, 21):
    tempres2 = res2final
    res2 = res2 + (k ** i) / fac(i)
    res2final = 1 / res2
    terror2 = (tvalue - res2final) / tvalue
    aerror2 = (res2final - tempres2) / res2final
    print("{:<20}{:<20}{:<20}".format("{}".format(round(res2final, 4)), "{}".format(round(terror2, 4)), "{}".format(round(aerror2, 4))))
    xs2.append(i)
    ys2.append(res2final)

plt.plot([item - 1 for item in xs2], [item - 1 for item in ys2])
plt.title("Second Approach")
plt.xlabel("Terms")
plt.ylabel("Value")
plt.show()
