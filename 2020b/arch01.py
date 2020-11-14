import numpy as np
import matplotlib.pyplot as plt

txt = np.loadtxt('datos01.dat')

plt.scatter(txt[:,0],txt[:,1])
plt.show()

print (txt)