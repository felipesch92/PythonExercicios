# Crie um módulo chamado moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
n = float(input('Valor: '))
print('O que deseja fazer?')
op = int(input('[1] Aumentar [2] Diminuir [3] Dobrar [4] Metade '))
if op == 1:
    a = float(input('Quanto deseja aumentar? '))
    r = moeda.aumentar(n, a)
    print(f'Valor {moeda.moeda(n)} com aumento de {moeda.moeda(a)} = {moeda.moeda(r)}')
elif op == 2:
    d = float(input('Quanto deseja diminuir? '))
    r = moeda.diminuir(n, d)
    print(f'Valor {moeda.moeda(n)} com diminuição de {moeda.moeda(d)} = {moeda.moeda(r)}')
elif op == 3:
    r = moeda.dobro(n)
    print(f'Valor {moeda.moeda(n)} dobrado = {moeda.moeda(r)}')
elif op == 4:
    r = moeda.metade(n)
    print(f'Valor {moeda.moeda(n)} sua metade: {moeda.moeda(r)}')
else:
    print('Opção inválida!')
