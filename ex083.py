# Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem correta.
exp = input('Digite a expressão: ')
cont = 0
for c in exp:
    if c == '(':
        cont += 1
    if c == ')':
        cont -= 1
if cont == 0:
    print(f'A expressão {exp} está correta! ')
else:
    print(f'A expressão {exp} está incorreta!')
