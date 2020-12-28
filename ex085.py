# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares
# e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
for x in range(0, 7):
    n = int(input(f'Digite o {x+1}o valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Números pares: {numeros[0]}')
print(f'Números ímpares: {numeros[1]}')
