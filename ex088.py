# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
numeros = []
for x in range(0, 6):
    while True:
        n = randint(1, 60)
        if n not in numeros:
            numeros.append(n)
            break
numeros.sort()
qtd_jogos = int(input('Quantos jogos? '))
jogos = []
for x in range(0, qtd_jogos):
    num_jogos = []
    for y in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in num_jogos:
                num_jogos.append(n)
                break
    num_jogos.sort()
    jogos.append(num_jogos)
print(f'Números da mega sena: {numeros}')
for j in jogos:
    c = 0
    for n in j:
        if n in numeros:
            c += 1
    print(f'No jogo {j} você acertou {c} números!')
    sleep(1)
