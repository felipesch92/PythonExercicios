# Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo a média
# de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
escola = []
while True:
    boletim = []
    aluno = input('Aluno: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    boletim.append(aluno)
    boletim.append(n1)
    boletim.append(n2)
    escola.append(boletim)
    if len(escola) > 2:
        break
print('*' * 30)
print('Boletim')
print('*' * 30)
for e in escola:
    print(f'{e[0]} Nota 1: {e[1]} Nota 2: {e[2]} Média: {(e[1] + e[2]) / 2}')
while True:
    op = input('Deseja Pesquisar um aluno? [S/N] ').upper()
    if op == 'N':
        break
    elif op == 'S':
        al = input('Nome do aluno: ')
        for e in escola:
            if al in e:
                if e[0] == al:
                    print(f'Nota 1: {e[1]} Nota 2: {e[2]} Média: {(e[1] + e[2]) / 2}')
    else:
        print('Opção inválida. Somente [S/N]')
