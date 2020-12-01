#Crie um programa que leia o nome de uma pessoa e diga se ela
# tem “SILVA” no nome.
n = str(input('Digite seu nome completo: ')).strip()
if 'SILVA' in n.upper():
    print('Seu nome possui Silva.')
else:
    print('Seu nome não possui Silva.')
