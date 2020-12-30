# Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
sala = []
for x in range(0, 3):
    n = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    aluno['nome'] = n
    aluno['nota1'] = n1
    aluno['nota2'] = n2
    aluno['media'] = (n1 + n2) / 2
    if aluno['media'] >= 7:
        aluno['situacao'] = 'aprovado'
    else:
        aluno['situacao'] = 'reprovado'
    sala.append(aluno.copy())
for s in sala:
    nome = s['nome']
    n1 = s['nota1']
    n2 = s['nota2']
    m = s['media']
    situacao = s['situacao']
    print(f'Nome: {nome}')
    print(f'Nota 1: {n1} Nota 2: {n1}')
    print(f'Média: {m:.2f} Você está {situacao}')
