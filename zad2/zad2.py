import matplotlib.pyplot as plt
import numpy as np


def kroki():
    enki = np.arange(20.)
    h0 = np.power(5., enki)
    h0 = 0.4 / h0
    return h0


def tabela(h1, x1):
    pochodna_rzeczywista = 1 / x1
    pochodna_przyblizona = np.float32((np.log(x1 + h1) - np.log(x1 - h1))) / np.float64(2 * h1)
    blad = np.abs(pochodna_rzeczywista - pochodna_przyblizona)
    tabela1 = np.mat((np.transpose(h1), np.transpose(pochodna_przyblizona), np.transpose(blad)))
    tabela2 = np.transpose(tabela1)
    print("     h                 pochodna         blad")
    print(tabela2)
    return blad


def minimal_blad(h2, blad):
    min_blad = np.min(blad)
    minimal = np.where(min_blad == blad)[0][0]
    print("\nMinimalny blad to " + str(min_blad) + " w wartosci " + str(h2[minimal]))


def plot(h3, blad):
    plt.plot(h3, blad)
    plt.plot(h3, blad, 'o')
    plt.title("Wykres zależności błędu od h")
    plt.xscale('log')
    plt.xlabel('h')
    plt.yscale('log')
    plt.ylabel('blad')
    plt.show()


x_init = 0.5
h_init = kroki()
blad_init = tabela(h_init, x_init)
minimal_blad(h_init, blad_init)
plot(h_init, blad_init)
