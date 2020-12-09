# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
c = 0
n = int(input('Informe um número entre 0 e 10: '))
n_m = randint(0, 10)
while n != n_m:
    c += 1
    if n > n_m:
        print('Menos..', end=' ')
    else:
        print('Mais..', end=' ')
    n = int(input('Tente novamente: '))
print('Foram necessárias {} tentativas para acertar.'.format(c))
