# Crie um programa que tenha a função leiaInt(), que vai funcionar
# de forma semelhante ‘a função input() do Python, só que fazendo a
# validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
# possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except Exception as erro:
            print(f'Não é um número válido. Erro: {erro}')
            continue
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except Exception as erro:
            print(f'Não é um número válido. Erro: {erro}')
            continue
        else:
            return num


n = leiaInt('Número: ')
print(n)
n = leiaFloat('Número: ')
print(n)
