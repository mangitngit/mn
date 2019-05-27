import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plocik(t, x, y, z):
    plt.figure(1)
    plt.subplot(3, 1, 1)
    plt.plot(t, x, "g", label="X")
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(t, y, "g", label="Y")
    plt.legend()
    plt.subplot(3, 1, 3)
    plt.plot(t, z, "g", label="Z")
    plt.legend()

    fig = plt.figure(2)
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z, "r")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def oblicz(t, x, y, z):
    fun_dx = lambda x, y, z: -10 * x + 10 * y
    fun_dy = lambda x, y, z: 28 * x - y - x * z
    fun_dz = lambda x, y, z: -8. / 3 * z + x * y

    t0 = 0
    tk = 25
    h = 0.03125

    while t0 < tk:
        k1_x = fun_dx(x[-1], y[-1], z[-1])
        k1_y = fun_dy(x[-1], y[-1], z[-1])
        k1_z = fun_dz(x[-1], y[-1], z[-1])

        k2_x = fun_dx(x[-1] + k1_x * h / 2, y[-1] + k1_y * h / 2, z[-1] + k1_z * h / 2)
        k2_y = fun_dy(x[-1] + k1_x * h / 2, y[-1] + k1_y * h / 2, z[-1] + k1_z * h / 2)
        k2_z = fun_dz(x[-1] + k1_x * h / 2, y[-1] + k1_y * h / 2, z[-1] + k1_z * h / 2)

        k3_x = fun_dx(x[-1] + k2_x * h / 2, y[-1] + k2_y * h / 2, z[-1] + k2_z * h / 2)
        k3_y = fun_dy(x[-1] + k2_x * h / 2, y[-1] + k2_y * h / 2, z[-1] + k2_z * h / 2)
        k3_z = fun_dz(x[-1] + k2_x * h / 2, y[-1] + k2_y * h / 2, z[-1] + k2_z * h / 2)

        k4_x = fun_dx(x[-1] + k3_x * h, y[-1] + k3_y * h, z[-1] + k3_z * h)
        k4_y = fun_dy(x[-1] + k3_x * h, y[-1] + k3_y * h, z[-1] + k3_z * h)
        k4_z = fun_dz(x[-1] + k3_x * h, y[-1] + k3_y * h, z[-1] + k3_z * h)

        x.append(x[-1] + h / 6 * (k1_x + 2 * (k2_x + k3_x) + k4_x))
        y.append(y[-1] + h / 6 * (k1_y + 2 * (k2_y + k3_y) + k4_y))
        z.append(z[-1] + h / 6 * (k1_z + 2 * (k2_z + k3_z) + k4_z))

        t0 += h
        t.append(t0)


t1, x1, y1, z1 = [0], [5], [5], [5]

oblicz(t1, x1, y1, z1)
plocik(t1, x1, y1, z1)
