# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
from time import sleep
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
maior = 0
op = 0
while op != 5:
    print('[1] Somar [2] Multiplicar [3] Maior [4] Novos números [5] Sair do programa')
    op = int(input('Opção: '))
    if op == 1:
        print('A soma de {} + {} é igual a = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação de {} * {} é igual a = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O número maior é o {}'.format(maior))
    elif op == 4:
        print('\n' * 100)
        n1 = float(input('Informe o primeiro número: '))
        n2 = float(input('Informe o segundo número: '))
    elif op == 5:
        print('Finalizando..')
        sleep(1)