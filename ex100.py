# Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
l = []


def sorteia():
    for x in range(0, 5):
        l.append(randint(0, 100))
    soma(l)


def soma(l):
    print(f'Lista dos números sorteados:')
    s = 0
    for n in l:
        print(n, end=' ')
        if n % 2 == 0:
            s += n
    print()
    print(f'A soma dos valores pares é de = {s}')


sorteia()
