#Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros
#termos dessa progressão.
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for x in range(0, 10):
    print(n, end=' ')
    n += r
