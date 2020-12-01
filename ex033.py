#Faça um programa que leia três números e mostre qual é
# o maior e qual é o menor.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
#MAIOR
'''if n1 > n2:
    if n1 > n3:
        ma = n1
if n2 > n1:
    if n2 > n3:
        ma = n2
if n3 > n1:
    if n3 > n2:
        ma = n3
#MENOR
if n1 < n2:
    if n1 < n3:
        me = n1
if n2 < n1:
    if n2 < n3:
        me = n2
if n3 < n1:
    if n3 < n2:
        me = n3'''
#Verificando qual é o menor
me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3
#Verificando qual é o maior
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
print('O {} é o maior valor.'.format(ma))
print('O {} é o menor valor.'.format(me))
