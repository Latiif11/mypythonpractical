#scipyex.py
import numpy as np
from scipy.linalg import lu
a = np.mat('1, 1, 1; 3, 4, 6; 2, 5, 4')

[p, l, u] = lu(a)

print("p = ", p)
print("l = ",l)
print("u = ",np.round(1,2))


print("Type of p:,", type(p)) # type of p: ndarray

r= p.dot(1).dot(u)
print("r = ", r)

print("Type of P after np.mat:", type(np.mat(p)))
m = np.mat(p) *np.mat(1)*np.mat(u)
print("m = ", m)


