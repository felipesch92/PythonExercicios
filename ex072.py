# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um
# número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
n_ex = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
        'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
        'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Informe um número para vê-lo por extenso: '))
    if 0 < n > 20:
        break
    print(n_ex[n])
