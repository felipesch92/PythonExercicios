# Crie um programa que declare uma matriz de dimensão
# 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
numeros = [[], [], []], [[], [], []], [[], [], []]
t = t_3 = maior = 0
for x in range(0, 3):
    for y in range(0, 3):
        numeros[x][y] = int(input(f'Número para a posição [{x}][{y}]: '))
for l in range(0, 3):
    numeros[l].sort()
    for c in range(0, 3):
        print(f'{numeros[l][c]:^5}', end='')
        if numeros[l][c] % 2 == 0:
            t += numeros[l][c]
        if c == 2:
            t_3 += numeros[l][c]
        if l == 1:
            if numeros[l][c] > maior:
                maior = numeros[l][c]
    print()
print(f'A soma dos pares é de: {t}')
print(f'A soma dos valores da terceira coluna é de: {t_3}')
print(f'O maior valor da segunda linha é: {maior} ou {numeros[1][2]}')
