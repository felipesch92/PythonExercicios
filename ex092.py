# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
# de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
cad_pessoas = []
from datetime import date
for x in range(0, 2):
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['ano'] = int(input('Ano Nascimento: '))
    pessoa['ct'] = int(input('Carteita de trabalho: '))
    if pessoa['ct'] != 0:
        pessoa['anoc'] = int(input('Ano Contratação: '))
        pessoa['sal'] = float(input('Salário: '))
    cad_pessoas.append(pessoa.copy())
for p in cad_pessoas:
    n = p['nome']
    ano = p['ano']
    ct = p['ct']
    print(f'Olá {n}, vejamos...')
    anos_trab = 0
    if ct != 0:
        anoc = p['anoc']
        sal = p['sal']
        anos_trab = date.today().year - anoc
        print(f'Seu salário é de R$ {sal}, contratado desde {anoc}')
        if anos_trab > 30:
            print('Você já pode se aposentar')
        else:
            print(f'Ainda faltam {30 - anos_trab} anos para você se aposentar')
print(cad_pessoas)
