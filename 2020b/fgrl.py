import math

def rx1(a,b,c):
   x = (-b + (b**2 -4 * a* c)**(1/2)) / (2*a)
   return x

def rx2(a,b,c):
   x = (-b - (b**2 -4 * a* c)**(1/2)) / (2*a)
   return x

a = complex( input('Dame el valor de A: ') ) 
b = complex( input('Dame el valor de B: ') )
c = complex( input('Dame el valor de C: ') )

#print ( 'Valores x1 = {:5.2f}, x2={:5.1f}'.format(rx1(a,b,c) ,rx2(a,b,c)) )
#print ('x1= %5.2f , y x2= %5.1f '%(rx1(a,b,c) ,rx2(a,b,c)))

print  (rx1(a,b,c) ,rx2(a,b,c)) 
