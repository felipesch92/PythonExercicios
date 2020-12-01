#Crie um programa que leia um número inteiro
#e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número inteiro:'))
if n % 2 == 0:
    print('\033[1;32;40m Número digitado é PAR')
else:
    print('\033[1;31;40m Número digitado é IMPAR')
