import numpy as np
import matplotlib.pyplot as plt


def step(x, u, A, B, C, D):
    steps = []
    for i in range(60):
        x_1 = A * x + B * u
        y = C * x_1 + D * u
        x = x_1
        steps.append(y.item(0))
    return steps


def lqr(c1, c2, A, B):
    Q = c1 * np.identity(3)
    R = c2
    P_1 = np.zeros((3, 3))
    P = P_1
    for i in range(20):
        P = Q + np.transpose(A) * (P_1 - P_1 * B * (R + np.transpose(B) * P_1 * B)**(-1) * np.transpose(B) * P_1) * A
        P_1 = P
    F = (R + np.transpose(B) * P * B) ** (-1) * np.transpose(B) * P * A
    return F


def un(x0, u, A, B, F):
    uk = []
    for i in range(50):
        xk = A * x0 + B * u
        x0 = xk
        uk_buf = -np.dot(F, xk)
        uk = np.append(uk, uk_buf)
    return uk


# zad 1
a2 = -3.85
a1 = 2.7
a0 = -0.45
A = np.matrix([[-a2, -a1, -a0], [1, 0, 0], [0, 1, 1]])
B = np.transpose(np.matrix([1, 0, 0]))
C = np.matrix([1, 1, 1])
D = [0]

# zad 2
X0 = 0
U = 1
y = step(X0, U, A, B, C, D)

# zad 3 i 4
c1 = 1000
c2 = 5
F = lqr(c1, c2, A, B)
A_1 = A - B * F
y_1 = step(X0, U, A_1, B, C, D)

un = un(X0, 1, A_1, B, F)

# ploty
plt.figure(1)
plt.subplot(311)
plt.plot(y)
plt.title("bez sterownika")

plt.subplot(312)
plt.plot(y_1)
plt.title("ze sterownikiem")

plt.subplot(313)
plt.plot(un)

plt.show()
