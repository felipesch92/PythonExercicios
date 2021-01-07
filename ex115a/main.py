import uteis
import ex115a
print('-' * 30)
print(f'MENU PRINCIPAL'.center(30))
print('-' * 30)
print('1 - Ver pessoas cadastradas')
print('2 - Cadastrar nova pessoa')
print('3 - Sair do sistema')
l_pessoa = []
ex115a.ola()
while True:
    op = input('Sua opção: ')
    if op in '0123':
        if op == '2':
            print('CADASTRO DE NOVA PESSOA')
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            l_pessoa.append(
                uteis.cad_pessoa(nome, idade)
            )
        elif op == '1':
            print('PESSOAS CADASTRADAS:')
            print(f'{"Nome":<20} Idade:')
            uteis.mostra_pessoa(l_pessoa)
        else:
            break
    else:
        print('Opção inválida!')

