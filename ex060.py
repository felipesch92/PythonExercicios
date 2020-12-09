# Faça um programa que leia um número qualquer
# e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Informe um número: '))
s = n
print('Calculando {}! = '.format(n), end='')
while n > 1:
    print('{}'.format(n), end='')
    print(' x ' if n > 2 else ' x 1 = ', end='')
    s = s * (n - 1)
    n -= 1
print('{}'.format(s))
