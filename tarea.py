import numpy as np
import matplotlib.pylab as plt
x= np.linspace(-2*np.pi,2*np.pi,10)
y= np.sin(x)
plt.ylabel('sen(x)')
plt.xlabel('x')
plt.plot(x,y)
plt.savefig('seno.png')
plt.show()