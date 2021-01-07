# Cadastrar pessoa
# ver pessoas cadastradas
def cad_pessoa(nome, idade):
    pessoa = {}
    pessoa['n'] = nome
    pessoa['i'] = idade
    return pessoa


def mostra_pessoa(l):
    for p in l:
        print(f'{p["n"]:<20} {p["i"]}')
