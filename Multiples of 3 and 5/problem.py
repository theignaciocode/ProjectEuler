suma = 0
numero = 0
while numero < 1000:
    if numero % 3 == 0 or numero % 5 == 0:
        suma += numero
    numero += 1
print(suma)
