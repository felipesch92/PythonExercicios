# Melhore o desafio 61 perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
x = 10
c = 0
while x > 0:
    print(p, end=' > ')
    p += r
    x -= 1
    c += 1
    if x < 1:
        print('Pausa')
        qtd_t = int(input('Quantos termos você quer mostrar a mais? '))
        if qtd_t > 0:
            x = qtd_t
print('Progressão finalizada com {} termos mostrados.'.format(c))
