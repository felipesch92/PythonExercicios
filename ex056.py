#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
s_i = 0
i_h_v = 0 #idade do homem mais velho
n_h_v = '' #Nome do homem mais velho
qtd_m = 0
for x in range(0, 4):
    n = input('Digite o nome da pessoa {}: '.format(x+1))
    i = int(input('Digite a idade da pessoa {}: '.format(x+1)))
    s = input('Digite o sexo da pessoa {}: '.format(x+1))
    s_i += i
    if s.upper() == 'M' and i > i_h_v:
        i_h_v = i
        n_h_v = n
    if s.upper() == 'F' and i < 20:
        qtd_m += 1
print('A média de idade do grupo é de: {} anos'.format(s_i // 4))
print('O nome do homem mais velho é {} e possui {} anos'.format(n_h_v, i_h_v))
print('{} Mulheres têm menos que 20 anos.'.format(qtd_m))
