import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

Nx = 100
Ny = 100
Mx = np.linspace(0.1, 0.9, Nx)
My = np.linspace(0.1, 0.9, Ny)
E = np.eye(100)

alfa = 1

# rv =multivariate_normal([0.5, -0.2], [[2.0, 0.3], [0.3, 0.5]])
# pos = np.dstack((Mx, My))
# T = np.zeros([100, 100])
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)
# ax2.contourf(Mx, My, rv.pdf(pos))

x, y = np.mgrid[-1:1:.01, -1:1:.01]
pos = np.dstack((x, y))
rv = multivariate_normal([0.5, 0.5], [[2.0, 2.3], [0.5, 0.5]])
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.contourf(x, y, rv.pdf(pos))

plt.show()
