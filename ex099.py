# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*valores):
    for p, v in enumerate(valores):
        if p == 0:
            maior = v
            p_maior = p
        elif v > maior:
            maior = v
            p_maior = p
    print(f'O número maior foi o número {maior} na posição {p_maior + 1}')


maior(8, 2, 4)
maior(1, 5, 2, 3, 10, 20, 2)
