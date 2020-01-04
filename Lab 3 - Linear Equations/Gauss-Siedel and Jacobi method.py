import numpy as np

Array = []
ResultArray = []
Solution = []

for i in range(3):
    r = []
    input1 = (input("Input equation {} coefficient: \n".format(i + 1)))
    for k in range(3):
        r.append(int(input1.split()[k]))
    Array.append(r)

input2 = (input("Input {} result coefficient: \n".format(i + 1)))
for k in range(3):
    ResultArray.append(int(input2.split()[k]))

t = []
input3 = (input("Input your approximate result: \n"))
for k in range(3):
    Solution.append(int(input3.split()[k]))

A = np.asarray(Array)
B = np.asarray(ResultArray)
x = np.asarray(Solution)
x0 = x
x1 = x
UwU = 0.95

U = np.triu(A, 1)
L = A - U
Li = np.linalg.inv(L)

D = np.diag(np.diag(A))
R = A - D
Di = np.linalg.inv(D)
Lr = L - D

print("A matrix: \n{}\n".format(A))
print("B matrix: \n{}\n".format(B))
print("Approximate result: \n{}\n".format(x))
print("Upper diagonal of A: \n{}\n".format(U))
print("Lower diagonal of A: \n{}\n".format(L))
print("Inverse of L: \n{}\n".format(Li))
print("Diagonal of A: \n{}\n".format(D))
print("Lower diagonal with relaxation of A: \n{}\n".format(Lr))

iter = int(input("Input iterations: \n"))

print("\nGauss-Siedel without relaxation: \n")
for i in range(iter):
    # Gauss-Siedel without relaxation
    Ux = np.dot(U, x)
    bUx = np.subtract(B, Ux)
    x = np.dot(Li, bUx)
    print("Iteration {}".format(i))
    print(x)

print("\nGauss-Siedel with relaxation = 0.95: \n")
for i in range(iter):
    # Gauss - Siedel with relaxation
    UwULr = np.multiply(Lr, UwU)
    DUwUL = D + UwULr
    DUwULi = np.linalg.inv(DUwUL)
    UwU1D = np.multiply((UwU - 1), D)
    UwUU = np.multiply(UwU, U)
    UwUUUwU1D = UwUU + UwU1D
    x1UwUUUwU1D = np.dot(UwUUUwU1D, x1)
    UwUB = np.multiply(UwU, B)
    UwUBx1UwUUUwU1D = UwUB - x1UwUUUwU1D
    x1 = np.dot(DUwULi, UwUBx1UwUUUwU1D)
    print("Iteration {}".format(i))
    print(x)

print("\nJacobi Method: \n")
for i in range(iter):
    # Jacobi Method
    Rx0 = np.dot(R, x0)
    BRx0 = np.subtract(B, Rx0)
    x0 = np.dot(Di, BRx0)

    print("Iteration {}".format(i))
    print(x)
