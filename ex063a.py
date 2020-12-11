n = 20
penultimo = 0
ultimo = 1
atual = 0
print('{} -'.format(penultimo), end='')
# Escreva um programa que leia um número N inteiro
# qualquer e mostre na tela os N primeiros elementos
# de uma Sequência de Fibonacci 0 – 1 – 1 – 2 – 3 – 5 – 8
while n > 1:
    penultimo = ultimo
    ultimo = atual
    atual = ultimo + penultimo
    print(' {} - '.format(atual), end='')
    n -= 1
print('FIM')
