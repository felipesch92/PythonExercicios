#Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
l1 = float(input('Primeira linha: '))
l2 = float(input('Segunda linha: '))
l3 = float(input('Terceira linha: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
