primeNumberFound = 10001
primeNumberCount = 0
number = 1
while primeNumberCount < primeNumberFound:
    number += 1
    contador = 0
    for numberTemp in range(2, int(number**(1/2))+1):
       if number % numberTemp == 0:
           contador += 1
           break
    if contador == 0:
        primeNumberCount += 1
print(number, primeNumberCount)
