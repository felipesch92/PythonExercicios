# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
d = 2
n = 0
c = 0
n_m = 0
l_d = ['PAR', 'IMPAR']
while True:
    while d != 0 and d != 1:
        d = int(input('Par[0] ou Impar[1]? '))
    n = int(input('Digite um número: '))
    n_m = randint(1, 5)
    print(f'{l_d[d]} entre {n} e {n_m} analisando.. ')
    if d == 0 and ((n + n_m) % 2 == 0):
        print('Venceu!')
        c += 1
    elif d == 1 and ((n + n_m) % 2 == 1):
        c += 1
        print('Venceu!')
    else:
        print('Perdeu!')
        break
    d = 2
if c > 0:
    print(f'Você venceu {c} vezes!')
else:
    print('A máquina te venceu!')
