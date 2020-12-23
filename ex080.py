# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
tmp = 0
while True:
    n = int(input('Valor: '))
    if len(numeros) == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1
    cond = input('Deseja continuar? [S/N]').upper()
    if cond == 'N':
        break
'''for x in range(0, len(numeros)):
    for x in range(0, len(numeros)):
        if x < len(numeros) - 1:
            if numeros[x] > numeros[x+1]:
                tmp = numeros[x]
                numeros[x] = numeros[x+1]
                numeros[x+1] = tmp'''
print(numeros)
