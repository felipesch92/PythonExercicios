# Crie um módulo chamado moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from utilidadesCeV import moeda, dado
n = dado.leiaDinheiro('Valor R$: ')
print('O que deseja fazer?')
op = int(input('[1] Aumentar [2] Diminuir [3] Dobrar [4] Metade '))
if op == 1:
    a = float(input('Quanto deseja aumentar? '))
    r = moeda.aumentar(n, a)
    print(f'Valor {n} com aumento de {a} = {r}')
elif op == 2:
    d = float(input('Quanto deseja diminuir? '))
    r = moeda.diminuir(n, d)
    print(f'Valor {n} com diminuição de {d} = {r}')
elif op == 3:
    r = moeda.dobro(n)
    print(f'Valor {n} dobrado = {r}')
elif op == 4:
    r = moeda.metade(n)
    print(f'Valor {n} sua metade: {r}')
else:
    print('Opção inválida!')
