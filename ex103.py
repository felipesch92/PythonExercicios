# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jogador='Padrão', gols=0):
    """
    -> Função que apresenta a ficha do jogador
    :param jogador: Nome do jogador
    :param gols: Quantidade de gols
    :return: sem retorno
    """
    print(f'O jogador {jogador} marcou {gols} gol(s)!')


ficha('Felipe', 0)
ficha(gols=10)
ficha('João')
ficha(gols=2, jogador='Fernando')
ficha()
help(ficha)
