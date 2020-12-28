ficha = list()
while True:
    n = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    ficha.append([n, [n1, n2], m])
    op = input('Deseja continuar? [S/N]').upper()
    if op == 'N':
        break
for f in ficha:
    print(f'{f[0]} Média: {f[2]}')
while True:
    op = input('Deseja pesquisar algum aluno? [S/N]').upper()
    c = 0
    if op == 'S':
        n = input('Aluno: ')
        for f in ficha:
            if n in f:
                if f[0] == n:
                    print(f'Nota 1: {f[1][0]} Nota 2: {f[1][1]} Média: {f[2]}')
                    c += 1
        if c == 0:
            print('Nome não encontrado na lista.')
    elif op == 'N':
        break
    else:
        print('Opção inválida. somente [S/N]')
