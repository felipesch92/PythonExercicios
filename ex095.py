# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
campeonato = []
while True:
    jogador['nome'] = input('Nome: ')
    jogos = int(input('Quantos jogos: '))
    if jogos != 0:
        partidas = []
        for j in range(0, jogos):
            g = int(input(f'Quantidade de gols no jogo {j+1}: '))
            partidas.append(g)
        jogador['jogos'] = partidas
    campeonato.append(jogador.copy())
    op = input('Deseja continuar [S/N]? ').upper()
    if op == 'N':
        break
print('cod nome            gols            :<15total')
cod = 0
for c in campeonato:
    t_gols = 0
    for j in c["jogos"]:
        t_gols += j
    print(f'{cod:>3} {c["nome"]:<15} {str(c["jogos"]):<15} {t_gols}')
    cod += 1
while True:
    op = input('Mostrar dados de qual jogador? (999) para parar ')
    if op != '999':
        for c in campeonato:
            if op in c['nome']:
                print(f'Analizando o jogador {c["nome"]}')
                for k, g in enumerate(c['jogos']):
                    print(f'No jogo {k+1} fez {g} gols.')
    else:
        break
