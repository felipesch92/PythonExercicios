# Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(lar, com):
    a = lar * com
    return a


lar = float(input('Largura: '))
com = float(input('Comprimento: '))
print(f'A área total do seu terreno é de : {area(lar, com):.2f} M2 ')
