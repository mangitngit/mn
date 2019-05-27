import scipy
import scipy.linalg as sci

Qa, Qb, Qc, Qd = 200, 300, 150, 350
ca, cb = 0.002, 0.002
Wg, Ws = 2.5, 1.5
E12, E23, E34, E35 = 50, 25, 50, 25

a1 = [Qa + E12, -E12, 0, 0, 0]
a2 = [-Qa - E12, Qa + Qb + E12 + E23, -E23, 0, 0]
a3 = [0, -Qa - Qb - E23, Qa + Qb + E23 + E35 + E34, -E34, -E35]
a4 = [0, 0, -Qc - E34, Qc + E34, 0]
a5 = [0, 0, -Qd - E35, 0, Qd + E35]

A = scipy.array([a1, a2, a3, a4, a5])
B = scipy.array([Ws + Qa * ca, Qb * cb, 0, 0, Wg])

L, U = sci.lu_factor(A)
wyn = sci.lu_solve((L, U), B)

B_new = scipy.array([800 + Qa * ca, Qb * cb, 0, 0, 1200])
wyn_new = sci.lu_solve((L, U), B_new)

print(wyn)
print(wyn_new)

A_1 = sci.inv(A)

grill = A_1[3, 4] * Wg * 100 / wyn[3]
palacze = A_1[3, 0] * Ws * 100 / wyn[3]
ulica = (Qa * ca * A_1[3, 0] + Qb * cb * A_1[3, 1]) * 100 / wyn[3]

print(grill, palacze, ulica)
