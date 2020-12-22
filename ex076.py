# Crie um programa que tenha uma tupla única com nomes de produtos e
# seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.
produtos = ('Lápis', 1.5, 'Borracha', 0.5, 'Caderno', 8.0,
            'Estojo', 15, 'Caneta', 2.5, 'Mochila', 35.00)
print('-'*20)
print('Listagem de preços')
print('-'*20)
for x, p in enumerate(produtos):
    if x % 2 == 0:
        print(f'{p:.<20}', end='')
    else:
        print(f'R$ {p:>5.2f}')
