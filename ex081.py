numeros = [7, 2, 6, 5, 10, 9, 15, 20, 16, 1, 8]
tmp = 0
for x in range(0, len(numeros)):
    for x in range(0, len(numeros)):
        if x < len(numeros) - 1:
            if numeros[x] > numeros[x+1]:
                tmp = numeros[x]
                numeros[x] = numeros[x+1]
                numeros[x+1] = tmp
    print(numeros[x])
print(numeros)
