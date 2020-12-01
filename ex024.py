# Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome “SANTO”.
cid = str(input('Digite o nome da cidade: ')).strip()
l_cid = cid.split()
if str.upper(l_cid[0]) == 'SANTO':
    print('A cidade começa com o nome Santo')
else:
    print('A cidade não começa com o nome Santo')
