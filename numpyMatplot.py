# numpyMatplot.py

import numpy as np
import matplotlib.pyplot as plt
# np.linspace: devide line from 0 to 4*pi into
x= np.linspace(0, 4*np.pi, 100)
sinx = np.sin(x) #Find sin(x) for above 100 pec
plt.plot(x,sinx) # plot (x sin(x))
plt.xlabel("Time") # label for axis
plt.ylabel("Amplitude") # lebel for y axis
plt.title('Sine wave') # title
plt.xlim([0, 4*np.pi]) # x-axis display range
plt.ylim([-1.5, 1.5]) #y-axis display
plt.show() #to show the plot on sceen


# arangeEx.py
import numpy as np
a=np.arange(1,10) # last elements i.e. 10 is not include
print(a) # the output will be [1 2 3 4 5 6 7 8 9]
print(a.shape) # (9) i.e total 9 enteries

b=np.arange(1,10,2) # print 1 to 10 with the spacing
print(b) #[1 2 4 ]
print(b.shape) # (5)

c=np.arange(10,2, -2)
print(c)
print(c.shape)

