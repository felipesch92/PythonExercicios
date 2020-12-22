# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
tmp = 0
while True:
    numeros.append(int(input('Valor: ')))
    cond = input('Deseja continuar? [S/N]').upper()
    if cond == 'N':
        break
    for x in range(0, len(numeros)):
        for x in range(0, len(numeros)):
            if x < len(numeros) - 1 and numeros[x] > numeros[x+1]:
                tmp = numeros[x]
                numeros[x] = numeros[x+1]
                numeros[x+1] = tmp
print(numeros)
