#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
from datetime import date
anos = []
ano_atual = date.today().year
for x in range(0, 7):
    nasc = int(input('Informe a data de nascimento da pessoa {}: '.format(x+1)))
    anos.append(ano_atual - nasc)
for x in range(0, 7):
    if anos[x] >= 18:
        print('A pessoa {} possui {} anos, já atingiu a maioridade'.format(x, anos[x]))
    else:
        print('A pessoa {} possui {} anos, ainda não atingiu a maioridade'.format(x, anos[x]))
