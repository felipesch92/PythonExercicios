#Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
n_c = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Adivinhe....')
n = int(input('Digite um número entre 0 e 5: '))
print('Processando...')
sleep(2)
if n_c == n:
    print('Você acertou o número que eu escolhi!')
else:
    print('Você nao acertou o número que eu escolhi!')
print('-=-' * 20)
