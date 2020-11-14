n = int (input('Cuantos numeros de fibonacii?'))

a, b = 0, 1

for x in range(n) :
    print(a)
    a, b = b, a+b