#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('Suas opções: \n [0] PEDRA \n [1] PAPEL \n [2] Tesoura')
op = int(input('Qual é a sua jogada? '))
op_c = randint(0, 2)
escolha = {
    0: 'Pedra',
    1: 'Papel',
    2: 'Tesoura'
}
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('Sua escolha: {}'.format(escolha[op]))
print('Escolha da máquina: {}'.format(escolha[op_c]))
if op != op_c:
    if (op == 0 and op_c == 2) or (op == 2 and op_c == 1) or (op == 1 and op_c == 0):
        print('Você venceu a máquina!')
    else:
        print('Você perdeu da máquina!')
else:
    print('Você empatou com a máquina!')
print('='*10)
