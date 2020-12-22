# Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.
numeros = []
for x in range(0, 5):
    numeros.append(int(input(f'valor {x+1}: ')))
maior = menor = p_maior = p_menor = numeros[0]
for x, n in enumerate(numeros):
    if n > maior:
        maior = n
        p_maior = x + 1
    if n < menor:
        menor = n
        p_menor = x + 1
print(f'Lista: {numeros}')
print(f'O maior número foi: {maior} na posição {p_maior}')
print(f'O menor número foi: {menor} na posição {p_menor}')
