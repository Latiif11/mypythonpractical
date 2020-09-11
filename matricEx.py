# matrixEx.py
import numpy as np
from scipy.linalg import lu

a= np.mat('1, 2: 3, 2: 2, 3')
a= np.mat('1, 2; 3, 2; 2, 3') # define matrix


aT= np.transpose(a)

b=2*np.eye(3)

c = b*a

l= lu(a)
print(l)
