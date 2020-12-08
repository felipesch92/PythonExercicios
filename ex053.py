#Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
# O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
f = input('Digite a frase: ').upper().replace(' ', '')
if f == f[::-1]:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
