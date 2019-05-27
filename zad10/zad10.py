from matplotlib import pyplot as plt
import numpy as np
from math import *

n = 40
tk = 2
step = tk/n
fnc = lambda T, Y: -3*Y*(T**2) + 3*Y

# Metoda analityczna
y, t = [], []
fnc2 = lambda T: 3*e**(-T**3 + 3*T)
for i in np.linspace(0, tk, n):
    t.append(i)
    y.append(fnc2(i))
plt.plot(t, y, label="anallitycznie")

# Metoda Eulera
y, t = [3], [0.]
for i in range(n):
    t.append((i + 1) * step)
    y.append(y[i] + fnc(t[i], y[i]) * step)
plt.plot(t, y, label="eulera")

# Metoda Heuna
y = [3]
for i in range(n):
    y_1 = y[i] + fnc(t[i], y[i]) * step
    y.append(y[i] + (fnc(t[i], y[i]) + fnc(t[i + 1], y_1)) / 2 * step)
plt.plot(t, y, label="heuna")

# Metoda punktu środkowego
y = [3]
for i in range(n):
    y_1 = y[i] + fnc(t[i], y[i]) * tk / (2 * n)
    y.append(y[i] + fnc(t[i] + tk / (2 * n), y_1) * step)
plt.plot(t, y, label="środkowy")

plt.legend()
plt.show()
