n = int (input('Cuantos numeros de fibonacii?'))

i = 0
a = 0
b = 1

while i < n :
    print(a)
    # genera la serie
    c = a + b 
    a = b
    b = c
    #Incremento de variable de control
    i = i + 1