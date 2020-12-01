#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome completo: ')).strip()
l_n = n.split()
p_n = l_n[0]
u_n = l_n[len(l_n)-1]
print('Seu primeiro nome é {}'.format(p_n))
print('Seu último nome é {}'.format(u_n))
