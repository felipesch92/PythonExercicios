#Exercício Python 20: O mesmo professor do desafio 19 quer
# sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada.
from random import shuffle
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
n_lista = [n1, n2, n3, n4]
#ordenada_lista = shuffle(n_lista)
#n_lista.sort()
shuffle(n_lista)
print('Lista dos alunos ordenados: {}'.format(n_lista))
