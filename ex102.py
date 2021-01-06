# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, mostra=True):
    """
    -> Função para calculo do fatorial de um número
    :param num: número a ser fatorado
    :param mostra: se irá mostrar o calculo ou somente o resultado final.
    :return:
    """
    i = 1
    l_fatorial = ''
    for x in range(num, 1, -1):
        i *= x
        if mostra:
            print(f'{x} *', end=' ')
            l_fatorial += f'{x} * '
    if mostra:
        print(f'1 = {i}')
        l_fatorial += f'1 = {i}'
    else:
        print(f'Resultado final: {i}')
    return l_fatorial

print(fatorial(5))
fatorial(10, False)
help(fatorial)
