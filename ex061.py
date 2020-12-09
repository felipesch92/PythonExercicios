# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
x = 10
while x > 0:
    print(n, end=' ')
    n += r
    x -= 1
    if x > 0:
        print('> ', end='')
print('FIM')
