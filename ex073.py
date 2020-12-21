# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('São Paulo', 'Flamengo', 'Atlético-MG', 'Internacional', 'Grêmio', 'Palmeiras',
'Fluminense', 'Santos', 'Ceará', 'Atlético-GO', 'Corinthians', 'Athletico-PR', 'Bragantino',
'Fortaleza', 'Sport', 'Bahia', 'Vasco', 'Botafogo', 'Coritiba', 'Goiás')
print(f'5 Primeiros times: {times[0:5]} ')
print(f'Últimos 4 colocados: {times[-4:]}')
times_ordenados = sorted(times)
print(f'Times em ordem alfabética: {times_ordenados}')
print(f'O Grêmio está na {times.index("Grêmio")+1} posição no campeonato Brasileiro!')
