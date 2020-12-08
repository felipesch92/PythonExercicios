#Faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
c = 0
if n == 1:
    c += 1
while n < 0:
    print('Digite um número válido: ')
    n = int(input('Digite um número inteiro: '))
for x in range(1, n+1):
    if n % x == 0:
        print('\033[33m', end='')
        c += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(x), end='')
print('\033[m')
if c == 2:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} não é primo!'.format(n))
