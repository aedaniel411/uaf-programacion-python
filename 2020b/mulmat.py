import numpy as np 

rA = int (input('Cuantos renglones de A ')) 
cA = int (input('Cuantas columnas de A '))

rB = cA 
cB = int(input ('Cuantas columnas de B '))

a = np.zeros((rA,cA))
b = np.zeros((rB,cB))

for r in range(rA) :
    for c in range(cA): 
        a[r,c] = float (input ('datos de A({:d},{:d})'.format(r,c)))

for r in range(rB) :
    for c in range(cB): 
        b[r,c] = float (input ('datos de B({:d},{:d})'.format(r,c)))

print(np.dot(a,b)) 
