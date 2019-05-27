import numpy as np
import matplotlib.pyplot as plt


def funkcja_pierwsza(x1):
    return 2 * x1 ** 2 + x1 - 3


def funkcja_druga(x2):
    return (-3 * x2 ** 2) / (3 - 2 * x2)


def funckja_glowna(x3):
    return -4 * x3 ** 3 + 7 * x3 ** 2 + 9 * x3 - 9


x = np.linspace(-5, 5, 1000)

y1 = funkcja_pierwsza(x)
y2 = funkcja_druga(x)
y3 = funckja_glowna(x)

plt.plot(x, y1, x, y2, x, y3)
plt.ylim(-50, 50)
plt.grid(True)


#  x1 = -1.3  y1 = -0.9
#  x2 = 0.75  y2 = -1.125
#  x3 = 2.3   y3 = 9.9


def iteracyjny(start_x, start_y):
    for i in range(0, 1000):
        start_x = np.sqrt((start_y - start_x + 3) / 2)
        start_y = np.sqrt((3 * start_y ** 2 + 3 * (start_x ** 2) * start_y) / (2 * start_x))
    print(start_x, start_y)


start_x_init = 1
start_y_init = 1

iteracyjny(start_x_init, start_y_init)

plt.show()
