# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:  escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~
def escreve(val):
    print('~'*len(val))
    print(val.upper())
    print('~'*len(val))


val = input('Digite algo: ')
escreve(val)
