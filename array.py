# arrayex.py
import numpy as np

a = np.array([1, 8, 2])
print(a) #[1 8 2]
print(np.shape(a)) #(3,)

b=np.array([
    [1,2],
    [3,4],
    [6, 2]
])
# b can be written ass follow as well but above is more readable
# b= np.array ([1,2])
print(np.shape(a))

#row of array can have different number of elements
c=np.array([[np.arange(1,10)],[np.arange(11, 16)]])
print(c)




