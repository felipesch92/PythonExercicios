#Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
peso = []
maior = 0
menor = 0
for x in range(0, 5):
    p = float(input('Informe o peso da pessoa número {}: '.format(x+1)))
    peso.append(p)
    if x == 0:
        maior = p
        menor = p
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print('Os pesos de forma ordenada são:')
peso = sorted(peso)
print(sorted(peso))
print('O menor peso é {}'.format(peso[0]))
print('O maior peso é {}'.format(peso[-1]))
print(menor, maior)
