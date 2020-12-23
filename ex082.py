# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
l_num = []
l_num_p = []
l_num_i = []
print('99 para sair')
while True:
    n = int(input('Número: '))
    if n == 99:
        break
    l_num.append(n)
for n in l_num:
    if n % 2 == 0:
        l_num_p.append(n)
    else:
        l_num_i.append(n)
print(f'Valores digitados: {l_num}')
print(f'Pares: {l_num_p}')
print(f'Ímpares: {l_num_i}')
