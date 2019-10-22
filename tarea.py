import numpy as np
import matplotlib.pylab as plt
x= np.linspace(-2*np.pi,2*np.pi,100)
y= np.cos(x)
plt.ylabel('cos(x)')
plt.xlabel('x')
plt.plot(x,y)
plt.savefig('coseno.png')
plt.show()