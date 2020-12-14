# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
n = ''
p = 0
t = 0
c = 0
b_p = 0  # preço produto mais barato
b_n = ''  # nome produto mais barato
while True:
    n = input('Nome do produto: ')
    p = float(input('Valor: '))
    if t == 0 or p < b_p:
        b_n = n
        b_p = p
    if p > 1000:
        c += 1
    t += p
    flag = ' '
    while flag not in 'SN':
        flag = input('Deseja continuar? [S/N] ').upper()[0]
    if flag == 'N':
        break
print(f'Total gasto na compra: R$ {t:.2f}')
print(f'{c} produtos custaram mais que R$ 1000,00')
print(f'{b_n} foi o produto mais barato custando R$ {b_p:.2f}')
