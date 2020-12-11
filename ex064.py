# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag).
l_n = []
n = 0
s = 0
while n != 999:
    n = int(input('Digite um valor inteiro: '))
    if n != 999:
        l_n.append(n)
print('Foram digitados {} números, sua soma é de: '.format(len(l_n)), end='')
for n in l_n:
    s += n
print(s)
