import numpy as np
from matplotlib import pyplot as pl


def analitic(x):
    y = np.arccos(x)
    return y


def expansion(n, x):
    denominator = np.cumprod(np.arange(2., (2. * n) + 1., 2.))  # [2,4,6,..] = (2n)
    denominator_two = np.arange(3., (2. * n + 1.) + 1., 2.)  # [3,5,7,..] = (2n+1)
    denominator = np.multiply(denominator, denominator_two)

    nominator = np.multiply(np.linspace(1., n, n), 2.)  # [2,4,...] = 2*n
    one = np.ones(n)
    nominator = np.add(nominator, one)  # [3,5,...] = 2*n + 1
    nominator = np.power(np.multiply(one, x), nominator)  # x^(2*n+1)
    nominator_two = np.cumprod(np.arange(1., (2. * n - 1.) + 1., 2.))  # [1,3,5,..] (2n-1)
    nominator = np.multiply(nominator, nominator_two)  # (2n-1)x^(2*n+1)

    y = (np.pi / 2.) - (x + np.sum(np.divide(nominator, denominator)))

    return y


vexpansion = np.vectorize(expansion)


def tabel(analytic, approx, x):
    print("arccos({})".format(x))
    for item in ["n", "analityczna", "przyblizona", "blad bezwzgledny", "blad wzgledny (%)"]:
        print("{:<30}".format(item), end='')
    print()

    analytic_x = analytic(x)
    for n in range(0, 10):
        approx_nx = approx(n, x)
        err = analytic_x - approx_nx
        rerr = err / analytic_x * 100
        for item in [n, analytic_x, approx_nx, err, rerr]:
            print("{:<30}".format(item), sep='', end='')
        print()


def graph(analytic, approx, x):
    pl.plot(x, analytic(x))
    for n in [0, 3, 10]:
        pl.plot(x, approx(n, x))
    pl.legend(["analityczna", "przyblizenie n=0", "przyblizenie n=3", "przyblizenie n=10"])
    pl.xlabel("x")
    pl.ylabel("f(x)")
    pl.title("Porownanie funkcji")
    pl.show()


tabel(analitic, vexpansion, 0.5)
graph(analitic, vexpansion, np.linspace(0, 1, 20))
