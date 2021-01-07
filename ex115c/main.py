import uteis
import arquivo
arq = 'bd.txt'
if arquivo.arquivo_existe(arq):
    print('Arquivo encontrado com sucesso!')
else:
    arquivo.criar_arquivo(arq)
print('-' * 30)
print(f'MENU PRINCIPAL'.center(30))
print('-' * 30)
print('1 - Ver pessoas cadastradas')
print('2 - Cadastrar nova pessoa')
print('3 - Sair do sistema')
while True:
    op = input('Sua opção: ')
    if op in '0123':
        if op == '2':
            print('CADASTRO DE NOVA PESSOA')
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            arquivo.cadastrar(arq, nome, idade)
        elif op == '1':
            # Listar conteúdo do arquivo
            print('PESSOAS CADASTRADAS:')
            arquivo.ler_arquivo(arq)
        else:
            break
    else:
        print('Opção inválida!')
