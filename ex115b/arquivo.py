def arquivo_existe(arq):
    try:
        a = open(arq, 'rt')
        a.close()
        return True
    except:
        return False


def criar_arquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')


def ler_arquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(a.read())
