import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fun(x,a,b) :
    return a / (x**b)

txt = np.loadtxt('datos01.dat')

res, mat = curve_fit (fun, txt[:,0],txt[:,1])

print (res) 
x = np.linspace( min(txt[:,0]), max(txt[:,0]), 50 ) 
y = fun(x,res[0], res[1])

plt.scatter(txt[:,0],txt[:,1])
plt.plot (x,y,color='red')
plt.show()