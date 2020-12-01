#Exercício Python 19: Um professor quer sortear um dos seus
# quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
al_1 = input('Primeiro aluno: ')
al_2 = input('Segundo aluno: ')
al_3 = input('Terceiro aluno: ')
al_4 = input('Quarto aluno: ')
al_lista = [al_1, al_2, al_3, al_4]
al_s = choice(al_lista)
print('O aluno sorteado foi: {} '.format(al_s))