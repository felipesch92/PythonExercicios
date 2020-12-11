# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.
l_n = []
n = 0
c = 's'.upper()
s = 0
maior = 0
menor = 0
media = 0
while c == 'S':
    n = int(input('Digite um número: '))
    l_n.append(n)
    c = input('Deseja continuar? [S/N] ').upper()
for n in l_n:
    s += n
    if n > maior:
        maior = n
    if menor == 0:
        menor = n
    elif n < menor:
        menor = n
media = sum(l_n) / len(l_n)
print('Você digitou {} números e a média é de: {:.2f}'.format(len(l_n), media))
print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))
