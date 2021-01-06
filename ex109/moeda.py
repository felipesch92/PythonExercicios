# aumentar(), diminuir(), dobro() e metade()
def aumentar(v, v_a, f=True):
    # v == Valor
    # v_a == Valor a aumentar
    v += v_a
    if f:
        return moeda(v)
    else:
        return v


def diminuir(v, v_d, f=True):
    # v == Valor
    # v_d == Valor a diminuir
    v -= v_d
    if f:
        return moeda(v)
    else:
        return v


def dobro(v, f=True):
    if f:
        return moeda(v*2)
    else:
        return v*2


def metade(v, f=True):
    if f:
        return moeda(v/2)
    else:
        return v/2


def moeda(v):
    return f'R$ {v:.2f}'.replace('.', ',')
