# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
c_l = [50, 20, 10, 5, 1]
q = 0
c = 0
v = int(input('Qual o valor a ser sacado? R$: '))
print('Seu saque: ')
while True:
    if (v // c_l[c]) > 0:
        q = v // c_l[c]
        v = (v % c_l[c])
        print(f'{q} cédulas de R$ {c_l[c]}')
    c += 1
    if v == 0:
        break
print('Volte sempre! Tenha um bom dia!')
