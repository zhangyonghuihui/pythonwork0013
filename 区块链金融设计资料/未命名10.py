import matplotlib.pyplot as plt
import numpy as np
a = plt.subplot(111,projection = 'polar')
t = np.linspace(0,2*np.pi,60)
a.plot(t,1-np.sin(t),'-',c='b')
plt.show()