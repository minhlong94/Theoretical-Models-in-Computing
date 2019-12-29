from numpy import interp
print("Program uses Newton's Interpol Poly method: ")
x = [0, 1, 2.5, 3, 4.5, 5, 6]
f = [2, 5.4375, 7.3516,7.5625, 8.4453, 9.1875, 12]
print(interp(3.5, x, f))