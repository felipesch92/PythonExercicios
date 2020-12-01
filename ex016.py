'''from math import trunc
n = input('Digite um número: ')
n_int = n.find('.')
n_int_math = trunc(float(n))
print('Número escolhido {}'.format(n))
print('Número na sua posição inteira: {}'.format(n[0:n_int]))
print('Posição inteira usando a função math.trunc: {}'.format(n_int_math))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
