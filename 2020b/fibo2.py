n = int (input('Cuantos numeros de fibonacii?'))

i = 0
a, b = 0, 1

while i < n :
    print(a)
    a, b = b, a+b

    i = i + 1