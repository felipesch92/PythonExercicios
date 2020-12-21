# Desenvolva um programa que leia quatro valores pelo
# teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
valores = [1, 2, 3, 4]
for x in range(0, 4):
    valores[x] = int(input('Valor: '))
valores = tuple(valores)
c_3 = 0
for x in range(0, 4):
    if valores[x] % 2 == 0:
        print(f'O {valores[x]} é par!')
if valores.count(3) > 0:
    print(f'O valor 3 apareceu na {valores.index(3)+1} posição!')
if valores.count(9) > 0:
    print(f'O número 9 apareceu {valores.count(9)} vezes!')
