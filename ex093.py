# Crie um programa que gerencie o aproveitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas partidas
# ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de
# gols feitos durante o campeonato.
jogador = {}
campeonato = []
for x in range(0, 2):
    jogador['nome'] = input('Nome: ')
    jogos = int(input('Quantos jogos: '))
    if jogos != 0:
        partidas = []
        for j in range(0, jogos):
            g = int(input(f'Quantidade de gols no jogo {j+1}: '))
            partidas.append(j+1)
            partidas.append(g)
        jogador['jogos'] = partidas
    campeonato.append(jogador.copy())
print(campeonato)
for c in campeonato:
    nome = c['nome']
    jogos = c['jogos']
    print(f'Vamos analisar o jogador {nome}')
    t = 0
    for k, j in enumerate(jogos):
        if k % 2 == 0:
            print(f'No jogo {j} foram ', end='')
        else:
            print(f'{j} gols')
            t += j
    print(f'No total foram {t} gols.')
