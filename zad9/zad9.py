import numpy as np
import scipy


def funkcja(x, n):
    return scipy.real(x**n * np.e**(w*x*1j))


def fun1(x, n):
    return x**n


def poch_fun1(x, n):
    return n*x**(n-1)


def fun2(x):
    return scipy.real(np.e**(w*x*1j))


def poch_fun2(x):
    return scipy.real(1j*w*np.e**(w*x*1j))


def oblicz(n, N, E, x):
    if n > 0:
        return N*x**n * (E/(w*1j))*np.e**(w*x*1j) - oblicz(n-1, n*N, E/(w*1j), x)
    else:
        return E/(w*1j) * np.e**(w*x*1j)


# n = 3
w = 100

for n_init in range(2, 11):
    print(n_init, oblicz(n_init, 1, 1, 10) - oblicz(n_init, 1, 1, 0))
