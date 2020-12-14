# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
i = 0
s = ''
c_18 = 0
c_h = 0
c_20 = 0
p = 0 #parar
while True:
    i = int(input('Informe a idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Informe o sexo: [M/F]')).upper()[0]
    if i > 18:
        c_18 += 1
    if s == 'M':
        c_h += 1
    if s == 'F' and i < 20:
        c_20 += 1
    p = ' '
    while p not in '01':
        p = str(input('Deseja continuar? [0-Não][1-Sim] '))
    if p == '0':
        break
print(f'{c_18} pessoas tem mais de 18 anos.')
print(f'{c_h} homens foram cadastrados.')
print(f'{c_20} mulheres tem menos de 20 anos.')
