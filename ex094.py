# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoa = {}
lista_pessoas = []
for x in range(0, 4):
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo M/F: ').upper()
    pessoa['idade'] = int(input('Idade: '))
    lista_pessoas.append(pessoa.copy())
print(f'No total {len(lista_pessoas)} pessoas foram cadastradas.')
m_i = 0
for p in lista_pessoas:
    m_i += p['idade']
m_i = m_i / len(lista_pessoas)
print(f'A média de idade entre as pessoas cadastradas foi de {m_i:.0f}')
for p in lista_pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} é mulher.')
for p in lista_pessoas:
    if p['idade'] > m_i:
        print(f'{p["nome"]} possui idade acima da média')
