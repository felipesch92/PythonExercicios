#Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input('Qual é a distância da viagem? '))
'''if km <= 200:
    v = km * 0.5
else:
    v = km * 0.45'''
v = km * 0.5 if km <= 200 else km * 0.45
print('Uma viagem de {} KM custa R$ {:.2f}'.format(km, v))
