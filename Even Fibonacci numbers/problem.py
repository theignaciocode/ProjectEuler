fibonacci = [1,2]
suma = 2
posicion = 2
while fibonacci[posicion-1] < 4000000:
    fibonacci.append(fibonacci[posicion-1] + fibonacci[posicion-2])
    if fibonacci[posicion] % 2 == 0:
        suma += fibonacci[posicion]
    posicion += 1
print(suma)
