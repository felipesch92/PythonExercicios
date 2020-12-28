# Crie um programa que declare uma matriz de dimensão
# 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
numeros = [[], [], []], [[], [], []], [[], [], []]
for x in range(0, 3):
    for y in range(0, 3):
        numeros[x][y] = int(input(f'Número para a posição [{x}][{y}]: '))
for l in range(0, 3):
    numeros[l].sort()
    for c in range(0, 3):
        print(f'{numeros[l][c]:^5}', end='')
    print()
