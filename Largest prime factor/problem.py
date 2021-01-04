buscar = 600851475143
primo = []
for numero in range(2,int(buscar**(1/2))+1):
    contador = 0
    for i in range(2, int(numero**(1/2))+1):
        if numero % i == 0:
            contador += 1
            break
    if contador == 0 and buscar % numero == 0:
        primo.append(numero)
print(max(primo))
