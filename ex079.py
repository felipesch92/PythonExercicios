# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.
valores = []
while True:
    n = int(input('Valor: (0 para parar) '))
    if n == 0:
        break
    if n not in valores:
        valores.append(n)
valores.sort()
print(valores)
