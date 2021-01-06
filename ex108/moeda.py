# aumentar(), diminuir(), dobro() e metade()
def aumentar(v, v_a):
    # v == Valor
    # v_a == Valor a aumentar
    v += v_a
    return v


def diminuir(v, v_d):
    # v == Valor
    # v_d == Valor a diminuir
    v -= v_d
    return v


def dobro(v):
    return v*2


def metade(v):
    return v/2


def moeda(v):
    return f'R$ {v:.2f}'.replace('.',',')
