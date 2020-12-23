# Crie um programa que vai ler vários números e colocar em uma lista.
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = []
print('Digite 99 para sair!')
while True:
    n = int(input('Número: '))
    if n == 99:
        break
    numeros.append(n)
print(f'Foram digitados {len(numeros)} números!')
print(f'Valores em ordem decrescente: ')
numeros.sort(reverse=True)
print(numeros)
if 5 in numeros:
    print('O número 5 está na lista!')
