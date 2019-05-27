from math import *
import matplotlib.pyplot as plt
from scipy.optimize import fmin

czas = []
odpowiedz = []
odpowiedz_teor = []


def wczytanie_z_pliku(czas_data, odpowiedz_data):
    for line in open("data8.txt").readlines():
        lines = line.split()
        czas_data.append(float(lines[0]))
        odpowiedz_data.append(float(lines[1]))


def odpowiedz_skokowa(t, tau1, zeta):
    return 1 - (e ** (-zeta / tau1 * t)) / sqrt(1 - zeta ** 2) * sin(sqrt(1 - zeta ** 2) * tau1 * t /
                                                                     atan(sqrt(1 - zeta ** 2) / zeta))


def odpowiedz_impulsowa(t, tau2, zeta):
    return e ** ((-zeta / tau2) * t) / (tau2 * sqrt(1 - zeta ** 2)) * sin(sqrt(1 - zeta ** 2) / tau2 * t)


def odpowiedz_teoretyczna(t, tau3, zeta, tau_z, k):
    return k * (tau_z * odpowiedz_impulsowa(t, tau3, zeta) + odpowiedz_skokowa(t, tau3, zeta))


def najmniejsze_kwadraty(parametry, time, y, Sr):
    for i, t in enumerate(time):
        Sr += (y[i] - odpowiedz_teoretyczna(t, parametry[0], parametry[1], parametry[2], parametry[3])) ** 2
    return Sr


def main():
    wczytanie_z_pliku(czas, odpowiedz)

    minimum = fmin(func=lambda func: najmniejsze_kwadraty(func, czas, odpowiedz, 0), x0=[0.9, 0.5, -0.9, 0.7])
    print(minimum)

    for n_time in czas:
        odpowiedz_teor.append(odpowiedz_teoretyczna(n_time, minimum[0], minimum[1], minimum[2], minimum[3]))

    plt.plot(czas, odpowiedz)
    plt.plot(czas, odpowiedz_teor, 'r--')
    plt.show()


if __name__ == "__main__":
    main()
