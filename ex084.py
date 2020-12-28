# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = []
tmp = []
mai = men = 0
while True:
    tmp.append(input('Nome: '))
    tmp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = tmp[1]
    else:
        if tmp[1] > mai:
            mai = tmp[1]
        if tmp[1] < men:
            men = tmp[1]
    pessoas.append(tmp[:])
    tmp.clear()
    if len(pessoas) == 3:
        break
print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'O maior peso foi de {mai} kilos', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {men} kilos', end=' ')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}', end= '')
