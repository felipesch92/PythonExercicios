# Crie um programa que tenha a função leiaInt(), que vai funcionar
# de forma semelhante ‘a função input() do Python, só que fazendo a
# validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    num = input(msg)
    if num.isnumeric():
        return int(num)
    else:
        print('ERRO, digite um número válido!')


n = leiaInt('Número: ')
print(n)