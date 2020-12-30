# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Felipe': randint(1,6),
        'Fernando': randint(1,6),
        'Dolores': randint(1, 6),
        'Tamara': randint(1, 6)}
jogo_organizado = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(jogo_organizado):
    print(f'{i+1}o lugar {v[0]} com {v[1]} pontos.')
    sleep(1)
