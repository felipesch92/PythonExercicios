#Faça um programa que calcule a soma entre todos os números que
#são impares e múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
c = 0
for x in range(3, 500, 3):
    if x % 2 == 1:
        print(x, end=' ')
        s += x
        c += 1
print('')
print('A soma dos {} valores é de: {}'.format(c, s))
