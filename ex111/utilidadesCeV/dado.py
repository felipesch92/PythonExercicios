def moeda(v):
    """
    -> Função para formatar o valor
    :param v: Valor
    :return: Valor formatado
    """
    return f'R$ {v:.2f}'.replace('.', ',')
