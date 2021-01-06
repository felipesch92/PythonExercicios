def moeda(v):
    """
    -> Função para formatar o valor
    :param v: Valor
    :return: Valor formatado
    """
    return f'R$ {v:.2f}'.replace('.', ',')


def leiaDinheiro(v):
    valido = False
    while not valido:
        entrada = input(v)
        if entrada.isnumeric():
            return float(entrada)
            valido = True
        else:
            print(f'\033[0;31mErro, {entrada} é um valor inválido! somente números![m')
