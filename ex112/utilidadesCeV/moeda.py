from ex111.utilidadesCeV import dado


def aumentar(v, v_a, f=True):
    """
    -> Função para aumentar valor
    :param v: Valor
    :param v_a: Valor a ser aumentado
    :param f: Formatar valor
    :return: valor
    """
    v += v_a
    if f:
        return dado.moeda(v)
    else:
        return v


def diminuir(v, v_d, f=True):
    """
    -> Função para diminuir valor
    :param v: Valor
    :param v_d: Valor a ser diminuido
    :param f: Se é para formatar valor
    :return: valor
    """
    v -= v_d
    if f:
        return dado.moeda(v)
    else:
        return v


def dobro(v, f=True):
    """
    -> Função que dobra o valor
    :param v: Valor
    :param f: Formatar
    :return: valor
    """
    if f:
        return dado.moeda(v*2)
    else:
        return v*2


def metade(v, f=True):
    """
    -> Função que diminui valor pela metade
    :param v: Valor
    :param f: Formatar
    :return: Valor
    """
    if f:
        return dado.moeda(v/2)
    else:
        return v/2
